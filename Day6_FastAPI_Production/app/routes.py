from fastapi import APIRouter
from fastapi import Header

from app.exceptions import UserNotFoundException
from app.models import User

router = APIRouter()

@router.get("/")
def home():
    return {"message":"API Working"}


@router.get("/header")
def read_header(
    user_agent: str = Header(None)
):
    return {
        "user_agent": user_agent
    }


@router.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise UserNotFoundException(user_id)

    return {
        "id":1,
        "name":"Hamna"
    }


@router.post("/users")
def create_user(user: User):
    return user