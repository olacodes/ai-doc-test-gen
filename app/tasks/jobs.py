import uuid
import shutil
import asyncio

from app.logger import setup_logger
from sqlalchemy.future import select

from app.services.code_fetcher import (
    clone_repo,
    collect_code_files,
    read_code_snippets,
)
from app.worker.celery_worker import celery_app
from app.models.job import DocumentationJob, JobStatus
from app.db.session import AsyncSessionLocal
from app.services.openai_llm import generate_docs_from_code
from app.services.storage import save_job_output

import logging

logger = setup_logger(__name__, level=logging.DEBUG)


# @celery_app.task(bind=True)
async def generate_documentation_task(job_data: dict):
    job_id = str(uuid.uuid4())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_job(job_data, job_id))
    await run_job(job_data, job_id)
    return {"job_id": job_id}


async def run_job(job_data: dict, job_id: str):
    async with AsyncSessionLocal() as session:
        try:
            job = DocumentationJob(
                id=job_id,
                repo_url=job_data.get("repo_url"),
                language=job_data["language"],
                generate_docs=job_data.get("generate_docs", True),
                generate_tests=job_data.get("generate_tests", True),
                status=JobStatus.PROCESSING,
            )
            session.add(job)
            await session.commit()

            repo_path = clone_repo(job_data["repo_url"])

            logger.info(f"Cloned repo to {repo_path}")

            code_paths = collect_code_files(repo_path, extensions=(".py", ".kt", ".js", ".java"))
            code_snippets = read_code_snippets(code_paths)

            logger.info(f"Collected {len(code_snippets)} code snippets")

            code_snippets_string = "\n\n".join(code_snippets)

            # Send to LLM
            docs, tests = await generate_docs_from_code(code_snippets_string, job_data)

            # Save to disk
            save_job_output(job_id, docs, tests)

            # Clean up repo
            shutil.rmtree(repo_path)

            # 4. Update job status
            job.status = JobStatus.COMPLETED
            await session.commit()

        except Exception as e:
            job.status = JobStatus.FAILED
            await session.commit()
            raise e
