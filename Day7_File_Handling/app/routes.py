from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    allowed_types = [
        "application/pdf"
    ]

    if file.content_type not in allowed_types:

        return {
            "error":
            "Only PDF files allowed"
        }

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message":
        "File uploaded successfully",
        "filename":
        file.filename
    }


from fastapi.responses import FileResponse

@router.get(
    "/download/{filename}"
)
def download_file(
    filename: str
):

    file_path = f"uploads/{filename}"

    return FileResponse(
        path=file_path,
        filename=filename
    )

from fastapi import Form
@router.post("/submit")
def submit_form(

    name: str = Form(...),

    email: str = Form(...)
):

    return {
        "name": name,
        "email": email
    }


from fastapi import BackgroundTasks

def write_log(message: str):

    with open("log.txt", "a") as f:
        f.write(message + "\n")


@router.post("/background")
def run_background_task(
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        write_log,
        "Task Executed"
    )

    return {
        "message":
        "Background Task Started"
    }