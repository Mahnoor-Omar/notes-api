from fastapi import APIRouter, status, Depends

from app.schemas.note import Note
from app.services.auth import get_current_user
from app.services.note_service import (
    create_new_note,
    get_notes,
    get_note,
    update_existing_note,
    delete_existing_note,
)

router = APIRouter(tags=["Notes"])


@router.post("/notes", status_code=status.HTTP_201_CREATED)
def create(
    note: Note,
    current_user=Depends(get_current_user)
):
    return create_new_note(note)


@router.get("/notes")
def read_all(
    current_user=Depends(get_current_user)
):
    return get_notes()


@router.get("/notes/{note_id}")
def read_one(
    note_id: int,
    current_user=Depends(get_current_user)
):
    return get_note(note_id)


@router.put("/notes/{note_id}")
def update(
    note_id: int,
    updated_note: Note,
    current_user=Depends(get_current_user)
):
    return update_existing_note(note_id, updated_note)


@router.delete("/notes/{note_id}")
def delete(
    note_id: int,
    current_user=Depends(get_current_user)
):
    return delete_existing_note(note_id)