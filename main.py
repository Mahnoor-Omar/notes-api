from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from config import settings

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
def home():
    return {"message": "Welcome to Notes API"}


# Create a note
@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: Note):
    notes.append(note)
    return note


# Get all notes
@app.get("/notes")
def get_notes():
    return notes


# Get a single note by ID
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


# Update a note
@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = updated_note
            return updated_note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


# Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            return {"message": "Note deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )