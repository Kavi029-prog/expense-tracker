from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from sqlalchemy import extract

from app.core.database import SessionLocal

from app.models.expense import Expense

from app.models.income import Income

from app.models.user import User

from app.core.security import get_current_user


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get("/summary")
def get_summary(

    month: str,

    db: Session = Depends(get_db),

    current_user: str = Depends(get_current_user)
):

    year, month_num = month.split("-")


    user = db.query(User).filter(

        User.username == current_user

    ).first()


    expenses = db.query(Expense).filter(

        Expense.owner_id == user.id,

        extract("year", Expense.expense_date) == int(year),

        extract("month", Expense.expense_date) == int(month_num)

    ).all()


    income = db.query(Income).filter(

        Income.owner_id == user.id,

        extract("year", Income.date) == int(year),

        extract("month", Income.date) == int(month_num)

    ).all()


    total_expenses = sum(

        expense.amount for expense in expenses
    )


    total_income = sum(

        item.amount for item in income
    )


    return {

        "total_income": total_income,

        "total_expenses": total_expenses,

        "net_balance": total_income - total_expenses
    }