# routes/user_routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.schemas import UserCreate, User
from database import get_db
import crud.user as crud
router = APIRouter()

# Create User
@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get User by ID
@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Update User
@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)

# Delete User
@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)
