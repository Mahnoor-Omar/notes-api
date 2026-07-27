from config import settings


def get_app_name():
    return settings.app_name


def get_notes_storage():
    from main import notes
    return notes