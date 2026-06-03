from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.users import router as user_router
from app.api.expenses import router as expense_router
from app.api.income import router as income_router
from app.api.categories import router as category_router
from app.api.summary import router as summary_router
from app.core.database import engine, Base
from app.models import expense, user, income, category
from app.models import expense, user, income, category
from app.api.users import router as auth_router


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(expense_router)
app.include_router(income_router)
app.include_router(category_router)
app.include_router(summary_router)

@app.get("/health")
def health():
    return {"status": "ok"}