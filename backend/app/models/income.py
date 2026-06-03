from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import Date

from sqlalchemy import ForeignKey

from app.core.database import Base


class Income(Base):

    __tablename__ = "income"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    amount = Column(Integer)

    source = Column(String)

    date = Column(Date)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )