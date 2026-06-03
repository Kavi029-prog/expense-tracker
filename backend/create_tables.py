from app.core.database import Base, engine

# Import ALL models

from app.models.user import User

from app.models.expense import Expense

from app.models.income import Income

from app.models.category import Category


print("Creating tables...")


Base.metadata.create_all(bind=engine)


print("Tables created successfully!")