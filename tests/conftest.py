import pytest
from fastapi.testclient import TestClient
from app.main import app, users_store
from httpx import AsyncClient, ASGITransport


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


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
async def async_test_user():
    return {
        'name': 'Alice Async', 'email': 'alice@async.com', 'age': 30,
    }
