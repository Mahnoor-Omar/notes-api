from fastapi import HTTPException

from app.repositories.note_repository import (
    create_note,
    get_all_notes,
    get_note_by_id,
    update_note,
    delete_note,
)
from app.schemas.note import Note


def create_new_note(note: Note):
    return create_note(note)


def get_notes():
    return get_all_notes()


def get_note(note_id: int):
    note = get_note_by_id(note_id)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


def update_existing_note(note_id: int, updated_note: Note):
    note = update_note(note_id, updated_note)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


def delete_existing_note(note_id: int):
    deleted = delete_note(note_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return {"message": "Note deleted successfully"}