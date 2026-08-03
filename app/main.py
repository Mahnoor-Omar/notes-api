from fastapi import FastAPI

from app.config import settings
from app.routers import auth, notes

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version
)

app.include_router(notes.router)
app.include_router(auth.router)