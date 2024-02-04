from sqlalchemy.orm import Session
from typing import List, Optional
from schemas.schemas import ProfileCreate
import models

def create_profile(db: Session, profile: ProfileCreate) -> models.Profile:
    db_profile = models.Profile(name=profile.name, description=profile.description)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile(db: Session, profile_id: int) -> Optional[models.Profile]:
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def update_profile(db: Session, profile_id: int, profile: ProfileCreate) -> Optional[models.Profile]:
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if db_profile:
        db_profile.name = profile.name
        db_profile.description = profile.description
        db.commit()
        db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: int) -> dict:
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()
        return {"message": "Profile deleted successfully"}
    return {"message": "Profile not found"}
