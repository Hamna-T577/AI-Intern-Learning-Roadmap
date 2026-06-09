def write_log(
    message: str
):

    with open(
        "log.txt",
        "a"
    ) as f:

        f.write(
            message + "\n"
        )

from fastapi import BackgroundTasks
from app.background_tasks import write_log
@router.post(
    "/background"
)
def run_background_task(

    background_tasks:
    BackgroundTasks

):

    background_tasks.add_task(

        write_log,

        "Task Executed"

    )

    return {
        "message":
        "Background Task Started"
    }