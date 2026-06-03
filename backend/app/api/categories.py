from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.models.category import Category

from app.models.user import User

from app.schemas.category import CategoryCreate

from app.core.security import get_current_user


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Create Category
@router.post("/categories")
def create_category(

    category: CategoryCreate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    new_category = Category(

        name=category.name,

        owner_id=user.id
    )

    db.add(new_category)

    db.commit()

    db.refresh(new_category)

    return {

        "message": "Category added",

        "category": new_category.name
    }


# Get Categories
@router.get("/categories")
def get_categories(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.username == current_user
    ).first()

    # Default categories
    default_categories = [

        "Food",

        "Transport",

        "Bills",

        "Shopping",

        "Salary",

        "Freelance"
    ]

    # User custom categories
    custom_categories = db.query(Category).filter(
        Category.owner_id == user.id
    ).all()

    custom_category_names = [

        category.name

        for category in custom_categories
    ]

    return {

        "default_categories": default_categories,

        "custom_categories": custom_category_names
    }