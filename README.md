# Notes API

A RESTful Notes API built with **FastAPI** that supports CRUD operations, JWT authentication using OAuth2 Password Flow, and automated API testing with **pytest** and **httpx**.

---

## Features

* Create, Read, Update, and Delete (CRUD) notes
* JWT Authentication with OAuth2 Password Flow
* Protected Notes endpoints
* Pydantic v2 request validation
* Layered project architecture:

  * Routers
  * Services
  * Repositories
* Interactive API documentation using Swagger UI
* Automated API tests with pytest and httpx

---

## Project Structure

```text
notes-api/
│
├── app/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── config.py
│   ├── dependencies.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_notes.py
│
├── .env
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* Pydantic v2
* OAuth2 Password Flow
* JWT (JSON Web Tokens)
* python-jose
* pytest
* pytest-asyncio
* httpx

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Mahnoor-Omar/notes-api.git
```

Navigate to the project directory:

```bash
cd notes-api
```

Install the dependencies:

```bash
uv sync
```

If you don't use `uv`, you can install dependencies with pip:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Authentication

This project uses **OAuth2 Password Flow** with **JWT** authentication.

To access protected Notes endpoints:

1. Open Swagger UI.
2. Use the **POST /login** endpoint with valid credentials.
3. Click the **Authorize** button.
4. Enter your credentials and authorize.
5. Swagger will automatically include the JWT token in subsequent requests.

After authorization, you can access all protected Notes endpoints.

---

## Running Tests

Run all tests:

```bash
pytest
```

Or run with verbose output:

```bash
pytest -v
```

The project includes automated tests for:

* Successful login
* Invalid login
* Creating a note with authentication
* Retrieving notes with authentication
* Unauthorized access to protected endpoints

---

## API Endpoints

### Authentication

| Method | Endpoint | Description                                      |
| ------ | -------- | ------------------------------------------------ |
| POST   | `/login` | Authenticate user and receive a JWT access token |

### Notes

| Method | Endpoint           | Description                           |
| ------ | ------------------ | ------------------------------------- |
| POST   | `/notes`           | Create a new note (Authenticated)     |
| GET    | `/notes`           | Retrieve all notes (Authenticated)    |
| GET    | `/notes/{note_id}` | Retrieve a note by ID (Authenticated) |
| PUT    | `/notes/{note_id}` | Update a note (Authenticated)         |
| DELETE | `/notes/{note_id}` | Delete a note (Authenticated)         |

---

## Future Improvements

* Store users and notes in a database
* Hash passwords using bcrypt
* Add user registration
* Implement refresh tokens
* Add pagination and filtering
* Increase automated test coverage
* Dockerize the application

---

## Author

**Mahnoor Omar**

This project was developed as part of a FastAPI backend learning milestone covering API development, authentication, project architecture, and automated testing.
