import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:
        yield client


async def get_access_token(client):
    response = await client.post(
        "/login",
        data={
            "username": "mahnoor",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_login_success(client):
    response = await client.post(
        "/login",
        data={
            "username": "mahnoor",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials(client):
    response = await client.post(
        "/login",
        data={
            "username": "mahnoor",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_note_authenticated(client):
    token = await get_access_token(client)

    response = await client.post(
        "/notes",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "id": 1,
            "title": "FastAPI",
            "content": "JWT Authentication",
        },
    )

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_notes_authenticated(client):
    token = await get_access_token(client)

    response = await client.get(
        "/notes",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_notes_unauthorized(client):
    response = await client.get("/notes")

    assert response.status_code == 401