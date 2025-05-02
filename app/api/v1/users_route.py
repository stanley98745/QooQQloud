from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserCreate, UserCreateResponse
from app.db.database import get_database_session
from app.models.models import User


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserCreateResponse)
def create_user(user: UserCreate, db: Session = Depends(get_database_session)):
    """
    Create a new User.
    """
    new_user = User(**user.dict())  # Unpack Pydantic model to dict
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user