from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_database_session
from app.models.models import RecordLog, Student, Class

router = APIRouter()

@router.get("/recordlogs/")
def get_record_logs(
    db: Session = Depends(get_database_session),
    student_name: str = None,
    class_name: str = None,
    sort_order: str = None,
    offset: int = 0,
    limit: int = 10
):
    """
    Fetch record logs with optional filters, sorting, and pagination.
    """
    query = db.query(RecordLog).join(Student).join(Class)
    if student_name:
        query = query.filter(Student.student_name.contains(student_name))
    if class_name:
        query = query.filter(Class.class_name.contains(class_name))
    if sort_order:
        query = query.order_by(sort_order)
    return query.offset(offset).limit(limit).all()

@router.post("/recordlogs/")
def create_record_log(record_data: dict, db: Session = Depends(get_database_session)):
    """
    Create a new record log.
    """
    new_record = RecordLog(**record_data)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.delete("/recordlogs/{log_id}")
def delete_record_log(log_id: int, db: Session = Depends(get_database_session)):
    """
    Delete a record log.
    """
    record_instance = db.query(RecordLog).filter(RecordLog.log_id == log_id).first()
    if not record_instance:
        raise HTTPException(status_code=404, detail="Record log not found")
    db.delete(record_instance)
    db.commit()
    return {"detail": "Record log deleted successfully"}
