# routes/profile_routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.schemas import ProfileCreate, Profile
from database import get_db
from crud import profile as crud

router = APIRouter()

# Create Profile
@router.post("/profile/", response_model=Profile)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

# Get Profile by ID
@router.get("/profile/{profile_id}", response_model=Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.get_profile(db=db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

# Update Profile
@router.put("/profile/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, profile: ProfileCreate, db: Session = Depends(get_db)):
    return crud.update_profile(db=db, profile_id=profile_id, profile=profile)

# Delete Profile
@router.delete("/profile/{profile_id}", response_model=dict)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    return crud.delete_profile(db=db, profile_id=profile_id)
