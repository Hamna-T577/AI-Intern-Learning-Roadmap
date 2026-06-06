from fastapi import FastAPI
from schemas.student_schema import Student

app = FastAPI()

students = []


@app.get("/")
def home():
    return {"message": "Welcome to Student API"}


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student Added",
        "data": student
    }


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student.id == student_id:
            return student

    return {"message": "Not Found"}


@app.get("/search")
def search_student(name: str):

    for student in students:

        if student.name == name:
            return student

    return {"message": "Not Found"}


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:

            students[index] = updated_student

            return {
                "message": "Student Updated",
                "data": updated_student
            }

    return {"message": "Student Not Found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Student Deleted",
                "data": deleted_student
            }

    return {"message": "Student Not Found"}