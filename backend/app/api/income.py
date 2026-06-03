from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.models.income import Income

from app.models.user import User

from app.schemas.income import (
    IncomeCreate,
    IncomeUpdate
)

from app.core.security import get_current_user


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Create Income
@router.post("/income")
def create_income(

    income: IncomeCreate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    new_income = Income(

        amount=income.amount,

        source=income.source,

        date=income.date,

        owner_id=user.id
    )

    db.add(new_income)

    db.commit()

    db.refresh(new_income)

    return {

        "message": "Income added",

        "income": new_income
    }


# Get Income
@router.get("/income")
def get_income(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    income = db.query(Income).filter(
        Income.owner_id == user.id
    ).all()

    return income


# Update Income
@router.put("/income/{income_id}")
def update_income(

    income_id: int,

    updated_income: IncomeUpdate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    income = db.query(Income).filter(

        Income.id == income_id,

        Income.owner_id == user.id

    ).first()

    if not income:

        return {
            "error": "Income not found"
        }

    income.amount = updated_income.amount

    income.source = updated_income.source

    income.date = updated_income.date

    db.commit()

    db.refresh(income)

    return {

        "message": "Income updated",

        "income": income
    }


# Delete Income
@router.delete("/income/{income_id}")
def delete_income(

    income_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    income = db.query(Income).filter(

        Income.id == income_id,

        Income.owner_id == user.id

    ).first()

    if not income:

        return {
            "error": "Income not found"
        }

    db.delete(income)

    db.commit()

    return {
        "message": "Income deleted"
    }