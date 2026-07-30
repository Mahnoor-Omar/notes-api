from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel

from app.config import settings
from app.dependencies import get_app_name, get_notes_storage

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version
)


# Pydantic model
class Note(BaseModel):
    id: int
    title: str
    content: str


# In-memory storage
notes = []


# Home route
@app.get("/")
def home(app_name: str = Depends(get_app_name)):
    return {
        "message": "Welcome to Notes API",
        "app": app_name
    }


# Create a note
@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(
    note: Note,
    notes_storage=Depends(get_notes_storage)
):
    notes_storage.append(note)
    return note


# Get all notes
@app.get("/notes")
def get_notes(
    notes_storage=Depends(get_notes_storage)
):
    return notes_storage


# Get a single note
@app.get("/notes/{note_id}")
def get_note(
    note_id: int,
    notes_storage=Depends(get_notes_storage)
):
    for note in notes_storage:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


# Update a note
@app.put("/notes/{note_id}")
def update_note(
    note_id: int,
    updated_note: Note,
    notes_storage=Depends(get_notes_storage)
):
    for index, note in enumerate(notes_storage):
        if note.id == note_id:
            notes_storage[index] = updated_note
            return updated_note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


# Delete a note
@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    notes_storage=Depends(get_notes_storage)
):
    for note in notes_storage:
        if note.id == note_id:
            notes_storage.remove(note)
            return {"message": "Note deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )