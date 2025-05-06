from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import opened_courses
from app.schemas.opened_courses import OpenedCourse, OpenedCourseCreate
from app.db.database import get_database_session as get_db

router = APIRouter(
    prefix="/opened_courses",
    tags=["opened_courses"],
)

@router.post("/", response_model=OpenedCourse)
def create_opened_course(opened_course: OpenedCourseCreate, db: Session = Depends(get_db)):
    return opened_courses.create_opened_course(db=db, opened_course=opened_course)

@router.get("/class/{class_id}", response_model=List[OpenedCourse])
def read_opened_courses_by_class_id(class_id: str, db: Session = Depends(get_db)):
    return opened_courses.get_opened_courses_by_class_id(db=db, class_id=class_id)
