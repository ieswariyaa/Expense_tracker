from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Expense, User
from app.schemas import ExpenseCreate, ExpenseOut
from app.routers.auth import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=ExpenseOut, status_code=201)
def create_expense(data: ExpenseCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    expense = Expense(**data.model_dump(), owner_id=user.id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

@router.get("/", response_model=list[ExpenseOut])
def list_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if skip < 0 or limit < 1 or limit > 100:
        raise HTTPException(422, "Invalid pagination values")
    return (db.query(Expense).filter(Expense.owner_id == user.id).offset(skip).limit(limit).all())

@router.get("/{expense_id}", response_model=ExpenseOut)
def get_expense(expense_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.owner_id == user.id).first()

    if not expense:
        raise HTTPException(404, "Expense not found")
    return expense

@router.put("/{expense_id}", response_model=ExpenseOut)
def update_expense(expense_id: int, data: ExpenseCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.owner_id == user.id).first()

    if not expense:
        raise HTTPException(404, "Expense not found")

    for key, value in data.model_dump().items():
        setattr(expense, key, value)
    db.commit()
    db.refresh(expense)
    return expense

@router.delete("/{expense_id}", status_code=204)
def delete_expense(expense_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.owner_id == user.id).first()

    if not expense:
        raise HTTPException(404, "Expense not found")
    db.delete(expense)
    db.commit()
    return Response(status_code=204)