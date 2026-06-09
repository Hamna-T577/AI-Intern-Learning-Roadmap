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

# Day 5 - Authentication & Security Basics

## Objective

Learn Authentication and Security concepts using FastAPI.

## Topics Covered

* Authentication
* Login API
* JWT Token Generation
* Protected Routes
* Security Basics

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Python-JOSE
* Passlib

## Project Structure

```text
Day5_Authentication/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## Features

* User Login
* JWT Token Generation
* Protected Endpoint
* Authentication Flow

## Installation

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

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| GET    | /        | Home            |
| POST   | /login   | User Login      |
| GET    | /profile | Protected Route |

## Learning Outcome

* Understand Authentication
* Understand JWT Tokens
* Secure APIs using Protected Routes
* Learn Security Basics in FastAPI

# Day 6 - FastAPI Production Features

## Objective

Learn how production-ready FastAPI applications are structured by implementing middleware, CORS configuration, headers, and centralized error handling.

---

## Topics Covered

- Middleware
- CORS Configuration
- Request Headers
- Global Exception Handling
- Custom Error Responses
- Pydantic Validation
- Swagger Documentation

---

## Project Structure

Day6_FastAPI_Production/

├── app/
│   ├── main.py
│   ├── routes.py
│   ├── middleware.py
│   ├── exceptions.py
│   └── models.py
│
├── requirements.txt

---

## Features Implemented

### 1. CORS Configuration

Configured CORS middleware to allow communication between frontend and backend applications.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Day 7 - File Handling and Background Tasks using FastAPI

## Objective

Learn how FastAPI handles file operations, form data, file validation, and background processing in a real-world backend application.

---

## Topics Covered

* File Upload
* File Download
* Form Data Handling
* File Validation
* Background Tasks

---

## Project Structure

```text
Day7_FileHandling/

├── app/
│   ├── main.py
│   ├── routes.py
│   ├── background_tasks.py
│
├── uploads/
├── log.txt
├── requirements.txt
```

---

## Features Implemented

### 1. File Upload API

Users can upload PDF files through Swagger UI.

Endpoint:

```http
POST /upload
```

Features:

* Accepts file uploads
* Stores uploaded files inside the uploads folder
* Returns upload confirmation

Example Response:

```json
{
  "message": "File uploaded successfully",
  "filename": "resume.pdf"
}
```

---

### 2. File Validation

Implemented validation to allow only PDF files.

Example:

Allowed:

```text
resume.pdf
```

Rejected:

```text
image.png
virus.exe
```

Example Response:

```json
{
  "error": "Only PDF files allowed"
}
```

---

### 3. File Download API

Users can download previously uploaded files.

Endpoint:

```http
GET /download/{filename}
```

Example:

```http
/download/resume.pdf
```

Returns the selected file for download.

---

### 4. Form Data Handling

Implemented form submission using FastAPI Form.

Endpoint:

```http
POST /submit
```

Input Fields:

* name
* email

Example Request:

```text
name = Hamna
email = hamna@gmail.com
```

Example Response:

```json
{
  "name": "Hamna",
  "email": "hamna@gmail.com"
}
```

---

### 5. Background Tasks

Implemented FastAPI BackgroundTasks to execute tasks after sending the response.

Endpoint:

```http
POST /background
```

Workflow:

```text
Client Request
      ↓
API Response Returned
      ↓
Background Task Executes
      ↓
Log Written to File
```

Example Response:

```json
{
  "message": "Background Task Started"
}
```

The background task writes:

```text
Task Executed
```

to log.txt.

---

## API Endpoints

| Method | Endpoint             | Description             |
| ------ | -------------------- | ----------------------- |
| POST   | /upload              | Upload PDF File         |
| GET    | /download/{filename} | Download File           |
| POST   | /submit              | Submit Form Data        |
| POST   | /background          | Execute Background Task |

---

## Learning Outcomes

After completing this task, I learned:

* How file uploads work in FastAPI
* How to save uploaded files on the server
* How file downloads are implemented
* How to validate uploaded files
* How form data is handled using Form()
* How FastAPI Background Tasks work
* How background processing improves API performance
* How to test APIs using Swagger UI

---

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```
