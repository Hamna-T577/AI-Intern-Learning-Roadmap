from fastapi import FastAPI
from database import engine, SessionLocal
from models.student import Base, Student
from schemas.student_schema import StudentCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Database Connected"}


# CREATE
@app.post("/students")
def create_student(student: StudentCreate):

    db = SessionLocal()

    new_student = Student(
        name=student.name,
        age=student.age
    )

    db.add(new_student)
    db.commit()

    return {"message": "Student Added"}


# READ ALL
@app.get("/students")
def get_students():

    db = SessionLocal()

    return db.query(Student).all()


# READ BY ID
@app.get("/students/{student_id}")
def get_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    if student:
        return student

    return {"message": "Student Not Found"}


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: StudentCreate):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        return {"message": "Student Not Found"}

    student.name = updated_student.name
    student.age = updated_student.age

    db.commit()

    return {"message": "Student Updated"}


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        return {"message": "Student Not Found"}

    db.delete(student)
    db.commit()

    return {"message": "Student Deleted"}