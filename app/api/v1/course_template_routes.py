# app/api/course_template_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.course_template_schema import CourseTemplateCreate, CourseTemplateOut
from app.crud.course_template_crud import (
    create_course_template,
    get_all_course_templates,
    get_templates_by_uploader,
    delete_course_template
)
from app.db.database import get_database_session as get_db
from app.api.v1.auth import get_current_user
from app.models.models import User

router = APIRouter(
    prefix="/course-templates",
    tags=["Course Templates"]
)


# 建立課程模板（僅限 admin 或 teacher）
@router.post("/", response_model=CourseTemplateOut)
def create_template(
        course: CourseTemplateCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="只有教師或管理者可建立課程")

    course.uploader_id = current_user.user_ID
    return create_course_template(db, course)


# 查詢所有課程模板（everyone）
@router.get("/", response_model=List[CourseTemplateOut])
def get_all_templates(db: Session = Depends(get_db)):
    return get_all_course_templates(db)


# 查詢使用者個人上傳的課程模板
@router.get("/mine", response_model=List[CourseTemplateOut])
def get_my_templates(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return get_templates_by_uploader(db, current_user.user_ID)


# 刪除課程模板（僅限 admin 或本人）
@router.delete("/{template_id}")
def delete_template(
        template_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return delete_course_template(db, template_id, current_user.user_ID, current_user.role)
