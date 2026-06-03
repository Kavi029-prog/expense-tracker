from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter()

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register user
@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "username": new_user.username
    }

# Login user
@router.post("/login")
def login_user(

    user: UserCreate,

    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    # User not found
    if not db_user:

        return {
            "error": "User not found"
        }

    # Wrong password
    if not verify_password(
        user.password,
        db_user.password
    ):

        return {
            "error": "Incorrect password"
        }

    # Create token
    access_token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }

# Protected profile route
@router.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Protected route accessed",
        "user": current_user
    }