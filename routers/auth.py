from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from db.database import get_database_session
from db.models import Teacher

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(user_credentials: dict, db: Session = Depends(get_database_session)):
    return {"message": "Login successful"}