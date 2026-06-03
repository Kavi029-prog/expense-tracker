from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.models.expense import Expense

from app.models.user import User

from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate
)
from app.core.security import get_current_user


router = APIRouter()


# Database connection
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Create Expense
@router.post("/expenses")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    new_expense = Expense(

        title=expense.title,

        amount=expense.amount,

        category=expense.category,

        note=expense.note,

        expense_date=expense.expense_date,

        owner_id=user.id
    )

    db.add(new_expense)

    db.commit()

    db.refresh(new_expense)

    return {
        "message": "Expense added successfully"
    }


# Get Expenses
@router.get("/expenses")
def get_expenses(

    category: str = None,

    start_date: str = None,

    end_date: str = None,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    query = db.query(Expense).filter(
        Expense.owner_id == user.id
    )

    # Filter by category
    if category:

        query = query.filter(
            Expense.category == category
        )

    # Filter by start date
    if start_date:

        query = query.filter(
            Expense.date >= start_date
        )

    # Filter by end date
    if end_date:

        query = query.filter(
            Expense.date <= end_date
        )

    expenses = query.all()

    return expenses

@router.put("/expenses/{expense_id}")
def update_expense(

    expense_id: int,

    updated_expense: ExpenseUpdate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    expense = db.query(Expense).filter(

        Expense.id == expense_id,

        Expense.owner_id == user.id

    ).first()

    if not expense:

        return {
            "error": "Expense not found"
        }

    expense.title = updated_expense.title

    expense.amount = updated_expense.amount

    expense.category = updated_expense.category

    expense.note = updated_expense.note

    expense.date = updated_expense.date

    db.commit()

    db.refresh(expense)

    return {

        "message": "Expense updated",

        "expense": expense
    }
# Delete Expense
@router.delete("/expenses/{expense_id}")
def delete_expense(

    expense_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    expense = db.query(Expense).filter(

        Expense.id == expense_id,

        Expense.owner_id == user.id

    ).first()

    if not expense:

        return {
            "error": "Expense not found"
        }

    db.delete(expense)

    db.commit()

    return {
        "message": "Expense deleted"
    }