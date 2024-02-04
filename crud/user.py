from sqlalchemy.orm import Session
from typing import List, Optional
from schemas.schemas import UserCreate
import models

def create_user(db: Session, user: UserCreate) -> models.User:
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: UserCreate) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> dict:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}
