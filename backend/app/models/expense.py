from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import ForeignKey

from sqlalchemy import Date

from app.core.database import Base


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    amount = Column(Integer)

    category = Column(String)

    note = Column(String)

    expense_date = Column(Date)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )