from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class CourseStatus(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed = "completed"

class OpenedCourseBase(BaseModel):
    class_id: str
    template_id: int
    status: CourseStatus = CourseStatus.not_started

class OpenedCourseCreate(OpenedCourseBase):
    pass

class OpenedCourse(OpenedCourseBase):
    id: int
    created_at: datetime
    status: Optional[CourseStatus] = CourseStatus.not_started

    class Config:
        from_attributes = True
