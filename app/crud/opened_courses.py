from sqlalchemy.orm import Session
from app.models.models import OpenedCourse
from app.schemas import opened_courses as oc_schemas

def create_opened_course(db: Session, opened_course: oc_schemas.OpenedCourseCreate):
    db_opened_course = OpenedCourse(**opened_course.dict())
    db.add(db_opened_course)
    db.commit()
    db.refresh(db_opened_course)
    return db_opened_course

def get_opened_courses_by_class_id(db: Session, class_id: str):
    return db.query(OpenedCourse).filter(OpenedCourse.class_id == class_id).all()
