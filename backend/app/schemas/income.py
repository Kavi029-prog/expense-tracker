from pydantic import BaseModel

from datetime import date


class IncomeCreate(BaseModel):

    amount: int

    source: str

    date: date


class IncomeUpdate(BaseModel):

    amount: int

    source: str

    date: date