import pytest
from sqlalchemy.orm import Session
from app.models.models import Class, CourseTemplate, OpenedCourse  # 對應你使用的三個模型


def test_create_and_query_opened_courses(db_session):
    # 模擬新增班級與課程模板
    new_class = Class(class_ID="1150010B002", class_name="測試班級", year=115)
    db_session.add(new_class)

    new_template = CourseTemplate(
        title="測試XR", description="XR課程", version="1.0",
        file_url="http://http://127.0.0.1:8080/", uploader_id=1, is_active=True
    )
    db_session.add(new_template)
    db_session.commit()

    # 插入 opened_course
    opened = OpenedCourse(class_id=new_class.class_ID, template_id=new_template.id)
    db_session.add(opened)
    db_session.commit()

    result = db_session.query(OpenedCourse).filter_by(class_id=new_class.class_ID).all()
    assert len(result) == 1
