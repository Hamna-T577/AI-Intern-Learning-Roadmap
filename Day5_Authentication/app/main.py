from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Day 5 - Auth & Security API",
    description="JWT Authentication with FastAPI - AI Intern Project",
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Day 5 Auth API is running!"}