import pytest
from fastapi.testclient import TestClient
from app.main import app, users_store

@pytest.fixture
def client():
    """各テスト前に users_store をリセット"""
    users_store.clear()  # テスト間の状態污染防止
    yield TestClient(app)
    users_store.clear()  # クリーンアップ

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
