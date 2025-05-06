from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.db.database import get_database_session
from app.models.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(user_credentials: dict, db: Session = Depends(get_database_session)):
    account = user_credentials.get("account")
    password = user_credentials.get("password")

    if not account or not password:
        raise HTTPException(status_code=400, detail="Missing account or password")

    user = db.query(User).filter(User.account == account).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 假設簽發 token（未來可換成 JWT）
    return {"access_token": f"token-for-{user.user_ID}", "token_type": "bearer", "user_id": user.user_ID}

# 模擬從「Header」取得登入用戶
def get_current_user(request: Request, db: Session = Depends(get_database_session)) -> User:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer token-for-"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        user_id = int(auth_header.split("Bearer token-for-")[1])
    except:
        raise HTTPException(status_code=401, detail="Invalid token format")

    user = db.query(User).filter(User.user_ID == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user