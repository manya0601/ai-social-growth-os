from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    task_id = Column(String, unique=True, index=True)  # celery task id
    status = Column(String)  # PENDING, SUCCESS, FAILURE

    task_type = Column(String)  # scrape, ai_generate, post_publish
    result = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)