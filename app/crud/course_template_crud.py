# app/crud/course_template_crud.py

from sqlalchemy.orm import Session
from app.models.models import CourseTemplate
from app.schemas.course_template_schema import CourseTemplateCreate
from fastapi import HTTPException, status

# 建立課程模板
def create_course_template(db: Session, course_data: CourseTemplateCreate) -> CourseTemplate:
    course = CourseTemplate(**course_data.dict())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

# 查詢所有課程模板（可給所有人查）
def get_all_course_templates(db: Session):
    return db.query(CourseTemplate).filter(CourseTemplate.is_active == True).all()

# 依上傳者查課程模板（教師或管理者使用）
def get_templates_by_uploader(db: Session, uploader_id: int):
    return db.query(CourseTemplate).filter(
        CourseTemplate.uploader_id == uploader_id,
        CourseTemplate.is_active == True
    ).all()

# 刪除課程模板（非真正刪除，是 soft delete）
def delete_course_template(db: Session, template_id: int, current_user_id: int, current_user_role: str):
    course = db.query(CourseTemplate).filter(CourseTemplate.id == template_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="課程模板不存在")

    if current_user_role != "admin" and course.uploader_id != current_user_id:
        raise HTTPException(status_code=403, detail="您無權限刪除此模板")

    course.is_active = False  # soft delete
    db.commit()
    return {"message": "課程模板已刪除"}
