import asyncio

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel

from config import settings
from dependencies import get_app_name, get_notes_storage

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version
)


class Note(BaseModel):
    id: int
    title: str
    content: str


notes = []


async def summarize_note(note: Note):
    await asyncio.sleep(2)

    if len(note.content) <= 50:
        return note.content

    return note.content[:50] + "..."


async def analyze_sentiment(note: Note):
    await asyncio.sleep(2)

    positive_words = ["good", "great", "love", "excellent", "happy"]

    for word in positive_words:
        if word.lower() in note.content.lower():
            return "Positive"

    return "Neutral"


async def extract_keywords(note: Note):
    await asyncio.sleep(2)

    words = note.content.split()

    return words[:5]


@app.get("/")
async def home(app_name: str = Depends(get_app_name)):
    return {
        "message": "Welcome to Notes API",
        "app": app_name
    }


@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(
    note: Note,
    notes_storage=Depends(get_notes_storage)
):
    await asyncio.sleep(2)

    notes_storage.append(note)

    return note


@app.get("/notes")
async def get_notes(
    notes_storage=Depends(get_notes_storage)
):
    await asyncio.sleep(1)

    return notes_storage


@app.get("/notes/{note_id}")
async def get_note(
    note_id: int,
    notes_storage=Depends(get_notes_storage)
):
    await asyncio.sleep(1)

    for note in notes_storage:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


@app.put("/notes/{note_id}")
async def update_note(
    note_id: int,
    updated_note: Note,
    notes_storage=Depends(get_notes_storage)
):
    await asyncio.sleep(2)

    for index, note in enumerate(notes_storage):
        if note.id == note_id:
            notes_storage[index] = updated_note
            return updated_note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


@app.delete("/notes/{note_id}")
async def delete_note(
    note_id: int,
    notes_storage=Depends(get_notes_storage)
):
    await asyncio.sleep(1)

    for note in notes_storage:
        if note.id == note_id:
            notes_storage.remove(note)

            return {
                "message": "Note deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


@app.get("/notes/{note_id}/analyze")
async def analyze_note(
    note_id: int,
    notes_storage=Depends(get_notes_storage)
):
    for note in notes_storage:
        if note.id == note_id:

            summary, sentiment, keywords = await asyncio.gather(
                summarize_note(note),
                analyze_sentiment(note),
                extract_keywords(note)
            )

            return {
                "id": note.id,
                "title": note.title,
                "summary": summary,
                "sentiment": sentiment,
                "keywords": keywords
            }

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )