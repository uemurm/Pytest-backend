import pytest

from tests.conftest import another_test_user


class TestUserCreateAsync:

    @pytest.mark.asyncio
    async def test_create_user(self, client, test_user):
        response = await client.post("/users", json=test_user)

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == test_user["name"]
        assert data["email"] == test_user["email"]
        assert "id" in data

    @pytest.mark.asyncio
    async def test_create_user_without_name(self, client):
        user = {
            'email': 'test@example.com',
            'age': 30,
        }
        response = await client.post("/users", json=user)

        assert response.status_code == 422  # Unprocessable Entity, ex. Validation Error

    @pytest.mark.parametrize('name,expected_status', [
        # Valid names
        ('A', 201), ('John', 201), ('Alice Johnson Smith', 201), ('A' * 100, 201),
        # Invalid names
        ('', 422), ('A' * 101, 422), ('A' * 200, 422),
    ])
    @pytest.mark.asyncio
    async def test_create_user_name_validation(self, client, test_user, name, expected_status):
        test_user['name'] = name
        response = await client.post('/users', json=test_user)

        assert response.status_code == expected_status

    @pytest.mark.parametrize("email,expected_status", [
        ("valid@example.com", 201),
        ("invalid.email", 422),  # Email validation fails
        ("", 422),
    ])
    @pytest.mark.asyncio
    async def test_create_user_email_validation(self, client, test_user, email, expected_status):
        """Test email validation"""
        test_user["email"] = email
        response = await client.post("/users", json=test_user)

        assert response.status_code == expected_status

    @pytest.mark.parametrize('age,expected_status', [
        # Valid ages
        (0, 201), (1, 201), (52, 201), (150, 201),
        # Invalid ages
        (-1, 422), (-100, 422), (151, 422), (200, 422)
    ])
    @pytest.mark.asyncio
    async def test_create_user_age_validation(self, client, test_user, age, expected_status):
        """Test age validation"""
        test_user['age'] = age
        response = await client.post('/users', json=test_user)

        assert response.status_code == expected_status


class TestUserReadAsync:
    @pytest.mark.asyncio
    async def test_list_users(self, client, test_user, another_test_user):
        await client.post("/users", json=test_user)
        await client.post("/users", json=another_test_user)

        response = await client.get("/users")

        assert response.status_code == 200
        assert len(response.json()) == 2


    @pytest.mark.asyncio
    async def test_get_user(self, client, test_user):
        create_response = await client.post("/users", json=test_user)
        user_id = create_response.json()["id"]

        get_response = await client.get(f"/users/{user_id}")

        assert get_response.status_code == 200
        assert get_response.json()["id"] == user_id


    @pytest.mark.asyncio
    async def test_get_nonexistent_user(self, client):
        response = await client.get("/users/999")

        assert response.status_code == 404



class TestUserUpdateAsync:

    @pytest.mark.asyncio
    async def test_update_nonexistent_user(self, client):
        response = await client.patch('/users/999', json={'name': 'New Name'})

        assert response.status_code == 404  # Resource not found
