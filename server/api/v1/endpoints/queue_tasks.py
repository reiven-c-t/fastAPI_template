from typing import Any, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from tasks.demo.demo_task import celery, demo_function

router = APIRouter()


class Body(BaseModel):
    weight: float
    height: float


class TaskStatus(BaseModel):
    id: str
    status: Optional[str]
    result: Optional[Any]


@router.post("/demo", response_model=TaskStatus)
def demo_api(body: Body) -> Any:
    task = demo_function.delay(weight=body.weight, height=body.height)
    return TaskStatus(id=task.id)


@router.get("/demo/{task_id}", response_model=TaskStatus)
def check_status(task_id: str) -> Any:
    result = celery.AsyncResult(task_id)
    status = TaskStatus(id=task_id, status=result.status, result=result.result)
    return status
