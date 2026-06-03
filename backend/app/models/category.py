from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import ForeignKey

from app.core.database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )