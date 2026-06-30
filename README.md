# Task Management API

A RESTful Task Management API built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

## Features

- Create tasks
- Retrieve all tasks
- Retrieve a single task
- Update tasks
- Delete tasks
- Filtering
- Pagination
- Custom error handling
- Request validation
- PostgreSQL database
- Alembic migrations

## Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

## Installation

### Clone the repository

```bash
git clone https://github.com/MmdrzaKing/SimpleTaskmaganementAPI
cd SimpleTaskmaganementAPI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Database

Create a PostgreSQL database

create a .env file and fill these in it:

```
DB_USERNAME=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```

## Run migrations

```bash
alembic upgrade head
```

## Start the server

```bash
uvicorn main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

## API Testing (Postman)

A Postman collection is included in this repository.

### How to use:
1. Open Postman
2. Import the file:
   `postman/Task Management API.postman_collection.json`
3. Run requests:
   - Create task
   - Get all tasks
   - Get one task
   - Update task
   - Delete task



## Curl examples:

Create

```bash
curl -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Study FastAPI\",\"status\":\"pending\"}"

```

Get all

```bash
curl http://127.0.0.1:8000/tasks
```

Get one

```bash
curl http://127.0.0.1:8000/tasks/1
```

Update

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
-H "Content-Type: application/json" \
-d "{\"status\":\"done\"}"
```

Delete

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```