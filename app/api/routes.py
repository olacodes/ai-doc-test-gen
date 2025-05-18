import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.logger import setup_logger
from app.models.schemas import CodeUploadRequest, JobResponse
from app.services.storage import get_job_output
from app.tasks.jobs import generate_documentation_task


router = APIRouter(prefix="/jobs", tags=["Jobs"])
logger = setup_logger(__name__, level=logging.DEBUG)


@router.post("/generate", response_model=JobResponse)
async def create_job(request: CodeUploadRequest, background_tasks: BackgroundTasks):
    # Enqueue job
    logger.info(f"Received job request: {request}")
    task = await generate_documentation_task(request.dict())
    return JobResponse(job_id=task.id, status="queued")


@router.get("/jobs/{job_id}/result")
async def get_job_result(job_id: str):
    try:
        result = get_job_output(job_id)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
