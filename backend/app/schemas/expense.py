from pydantic import BaseModel

from typing import Optional

from datetime import date


class ExpenseCreate(BaseModel):

    title: str

    amount: float

    category: str

    note: Optional[str] = None

    expense_date: Optional[date] = None


class ExpenseUpdate(BaseModel):

    title: str

    amount: float

    category: str

    note: Optional[str] = None

    expense_date: Optional[date] = None