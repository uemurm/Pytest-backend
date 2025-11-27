import pytest
from app.main import app
from httpx import AsyncClient, ASGITransport


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
async def test_user():
    return {
        'name': 'Alice', 'email': 'alice@async.com', 'age': 30,
    }


@pytest.fixture
async def another_test_user():
    return {
        'name': 'Bob', 'email': 'bob@async.com', 'age': 40,
    }
