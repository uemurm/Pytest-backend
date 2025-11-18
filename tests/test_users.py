import pytest


class TestUserCRUD:
    """User CRUD のテスト群"""

    def test_create_user(self, client, test_user):
        """正常系：ユーザー作成"""
        response = client.post("/users", json=test_user)

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == test_user["name"]
        assert data["email"] == test_user["email"]
        assert "id" in data

    def test_list_users(self, client, test_user, another_test_user):
        """正常系：ユーザー一覧"""
        client.post("/users", json=test_user)
        client.post("/users", json=another_test_user)

        response = client.get("/users")

        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_nonexistent_user(self, client):
        """エラー系：存在しないユーザー取得"""
        response = client.get("/users/999")

        assert response.status_code == 404

    @pytest.mark.parametrize("email,expected_status", [
        ("valid@example.com", 201),
        ("invalid.email", 422),  # バリデーション失敗
        ("", 422),
    ])
    def test_create_user_validation(self, client, test_user, email, expected_status):
        """バリデーション：メールアドレス"""
        test_user["email"] = email
        response = client.post("/users", json=test_user)
        assert response.status_code == expected_status
