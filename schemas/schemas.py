from pydantic import BaseModel
from typing import List, Optional

class ProfileBase(BaseModel):
    name: str
    description: str

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    profiles: List[Profile] = []

    class Config:
        orm_mode = True
