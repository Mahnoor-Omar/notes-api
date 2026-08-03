from app.models.user import User


fake_users = {
    "mahnoor": User(
        username="mahnoor",
        password="password123"
    )
}


def get_user(username: str) -> User | None:
    return fake_users.get(username)