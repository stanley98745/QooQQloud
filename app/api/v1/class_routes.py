from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_database_session
from app.models.models import Class
from app.schemas.class_schema import ClassCreate, ClassUpdate, ClassResponse
from typing import List

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.get("/", response_model=List[ClassResponse])
def get_classes(db: Session = Depends(get_database_session),
                search_class_name: str = None,
                offset: int = 0,
                limit: int = 10):
    """
    Fetch classes with optional search term and pagination.
    """
    query = db.query(Class)
    if search_class_name:
        query = query.filter(Class.class_name.contains(search_class_name))
    return query.offset(offset).limit(limit).all()

@router.post("/", response_model=ClassResponse)
def create_class(class_data: ClassCreate, db: Session = Depends(get_database_session)):
    """
    Create a new class.
    """
    new_class = Class(**class_data.dict())  # Unpack Pydantic model to dict
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@router.put("/{class_ID}", response_model=ClassResponse)
def update_class(class_ID: str, class_data: ClassUpdate, db: Session = Depends(get_database_session)):
    """
    Update an existing class.
    """
    class_instance = db.query(Class).filter(Class.class_ID == class_ID).first()
    if not class_instance:
        raise HTTPException(status_code=404, detail="Class not found")
    for key, value in class_data.dict().items():
        setattr(class_instance, key, value)
    db.commit()
    db.refresh(class_instance)
    return class_instance

@router.delete("/{class_ID}")
def delete_class(class_ID: str, db: Session = Depends(get_database_session)):
    """
    Delete a class.
    """
    class_instance = db.query(Class).filter(Class.class_ID == class_ID).first()
    if not class_instance:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(class_instance)
    db.commit()
    return {"detail": "Class deleted successfully"}
