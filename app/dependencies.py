from app.config import settings


def get_app_name():
    return settings.app_name


def get_notes_storage():
    from app.main import notes
    return notes