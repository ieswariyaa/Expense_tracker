from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import auth, expenses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API", description="Expense CRUD API with JWT authentication", version="1.0.0")

app.include_router(auth.router)
app.include_router(expenses.router)

@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}