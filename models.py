from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="profiles")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    
    profiles = relationship("Profile", back_populates="owner", cascade="all, delete")
    favorite_profiles = relationship("Profile", secondary="favorite_profiles")

class FavoriteProfiles(Base):
    __tablename__ = 'favorite_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'), primary_key=True)

