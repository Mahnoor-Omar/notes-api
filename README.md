# Notes API

A simple RESTful Notes API built with **FastAPI**. This project demonstrates CRUD (Create, Read, Update, Delete) operations using in-memory storage and data validation with **Pydantic v2**.

## Features

* Create a note
* View all notes
* View a single note by ID
* Update an existing note
* Delete a note
* Request validation using Pydantic v2
* Interactive API documentation with Swagger UI and ReDoc

## Technologies Used

* Python 3
* FastAPI
* Pydantic v2
* Pydantic Settings
* Uvicorn

## Project Structure

```text
notes-api/
├── .env
├── .gitignore
├── config.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Mahnoor-Omar/notes-api.git
```

2. Navigate to the project directory:

```bash
cd notes-api
```

3. Create and activate a virtual environment (if needed).

4. Install the dependencies:

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root with the following values:

```text
APP_NAME=Notes API
DEBUG=True
API_VERSION=v1
```

## Running the Application

Start the development server with:

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/`                | Welcome message       |
| POST   | `/notes`           | Create a new note     |
| GET    | `/notes`           | Retrieve all notes    |
| GET    | `/notes/{note_id}` | Retrieve a note by ID |
| PUT    | `/notes/{note_id}` | Update a note         |
| DELETE | `/notes/{note_id}` | Delete a note         |

## Example Note

```json
{
  "id": 1,
  "title": "Shopping",
  "content": "Buy milk"
}
```

## Notes

* Notes are stored in memory using a Python list.
* Data is not persisted after the server is stopped or restarted.
* Input data is automatically validated using Pydantic v2.

## Author

**Mahnoor Omar**
