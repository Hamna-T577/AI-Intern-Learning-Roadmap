from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.exceptions import UserNotFoundException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(
    UserNotFoundException
)
async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error":
            f"User {exc.user_id} not found"
        }
    )

app.include_router(router)