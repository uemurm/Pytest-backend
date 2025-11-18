import pytest
from fastapi.testclient import TestClient
from app.main import app, users_store

@pytest.fixture
def client():
    """Reset users_store before each test"""
    users_store.clear()
    yield TestClient(app)
    users_store.clear()

@pytest.fixture
def test_user():
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }

@pytest.fixture
def another_test_user():
    return {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "age": 25
    }
