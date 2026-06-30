from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.schemas import TaskCreate, TaskUpdate
from database.database import get_db
from services.service import (
    create_task as service_create_task, 
    get_tasks as service_get_tasks, 
    get_task_by_id as service_get_task_by_id, 
    update_task as service_update_task, 
    delete_task as service_delete_task
)

router = APIRouter()

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate, 
    db: Session = Depends(get_db)
):
    return service_create_task(task, db)


@router.get("/tasks")
def get_tasks(
    status: str | None = None,
    priority: str | None = None,
    sort: str | None = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return service_get_tasks(status, priority, sort, page, limit, db)


@router.get("/tasks/{id}")
def get_task(
    id: int,
    db: Session = Depends(get_db)
):
    return service_get_task_by_id(id, db)


@router.put("/tasks/{id}")
def update_task(
    id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    return service_update_task(id, task, db)


@router.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    id: int,
    db: Session = Depends(get_db)
):
    return service_delete_task(id, db)