from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class JobStatus(str, enum.Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class DocumentationJob(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    repo_url = Column(String, nullable=True)
    language = Column(String, nullable=False)
    generate_docs = Column(Boolean, default=True)
    generate_tests = Column(Boolean, default=True)
    status = Column(Enum(JobStatus), default=JobStatus.QUEUED)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
