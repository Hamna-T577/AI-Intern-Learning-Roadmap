## Day 1 - OOP & Error Handling

### Run

```bash
cd Day1_OOP_ErrorHandling
python main.py
```

---

## Day 2 - Advanced Python Features

### Run

```bash
cd Day2_Advanced_Python
python main.py
```

---

## Day 3 - FastAPI CRUD

### Run

```bash
cd Day3_FastAPI_CRUD

python -m venv venv
venv\Scripts\activate

pip install fastapi uvicorn pydantic

uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```





# Day 4 - Database Integration with FastAPI and PostgreSQL

## Objective

Learn how to connect FastAPI with PostgreSQL using SQLAlchemy ORM and perform CRUD operations.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

## Project Structure

```text
Day4_Database_Integration/
│
├── main.py
├── database.py
├── .env
├── requirements.txt
│
├── models/
│   └── student.py
│
├── schemas/
│   └── student_schema.py
│
└── README.md
```

---

## Features

- Database Connection
- Student Model
- Pydantic Schema
- Create Student
- Get All Students
- Get Student By ID
- Update Student
- Delete Student

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /students | Create Student |
| GET | /students | Get All Students |
| GET | /students/{id} | Get Student By ID |
| PUT | /students/{id} | Update Student |
| DELETE | /students/{id} | Delete Student |

---

## Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

