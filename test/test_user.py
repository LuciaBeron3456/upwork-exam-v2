from fastapi.testclient import TestClient
from main import app
from app.db.session import SessionLocal
from app.db import crud
from app.schemas.user import UserCreate
import pytest

# Define the client fixture
@pytest.fixture
def client():
    return TestClient(app)

# Define the sample user data fixture
@pytest.fixture
def sample_user_data():
    return {
        "email": "user1@example.com",
        "username": "user1",
        "age": 25
    }

# Define the test function for GET request
def test_get_user(client, sample_user_data):
    # Create a user for testing
    db = SessionLocal()
    user = crud.create_user(db=db, user=UserCreate(**sample_user_data))
    db.close()

    response = client.get(f"/api/users/{user.id}")
    assert response.status_code == 200
    assert response.json()["email"] == sample_user_data["email"]
    assert response.json()["username"] == sample_user_data["username"]
    assert response.json()["age"] == sample_user_data["age"]

# Define the test function for POST request
def test_post_user(client, sample_user_data):
    user_data = {
        "email": "updated_email@example.com",
        "username": "updated_username",
        "age": 40
    }

    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert response.json()["username"] == user_data["username"]
    assert response.json()["age"] == user_data["age"]
