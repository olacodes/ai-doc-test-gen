from app.logger import setup_logger
from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from app.models.schemas import CodeUploadRequest, JobResponse
from app.tasks.jobs import generate_documentation_task
import logging

router = APIRouter(prefix="/jobs", tags=["Jobs"])


logger = setup_logger(__name__, level=logging.DEBUG)


@router.post("/generate", response_model=JobResponse)
async def create_job(request: CodeUploadRequest, background_tasks: BackgroundTasks):
    # Enqueue job
    logger.info(f"Received job request: {request}")

    task = await generate_documentation_task(request.dict())

    return JobResponse(job_id=task.id, status="queued")
