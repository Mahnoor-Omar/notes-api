from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from app.services.auth import (
    authenticate_user,
    create_access_token,
)

from app.schemas.auth import Token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }