from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models import User
from app.schemas import LoginRequest
from app.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.username == data.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(user.username)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def me(username: str = Depends(get_current_user)):
    return {
        "username": username
    }