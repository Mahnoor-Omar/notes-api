from app.schemas.note import Note

notes = []


def create_note(note: Note):
    notes.append(note)
    return note


def get_all_notes():
    return notes


def get_note_by_id(note_id: int):
    for note in notes:
        if note.id == note_id:
            return note
    return None


def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = updated_note
            return updated_note
    return None


def delete_note(note_id: int):
    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            return True
    return False