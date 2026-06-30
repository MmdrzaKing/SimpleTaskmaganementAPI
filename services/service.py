from datetime import datetime
from sqlalchemy.orm import Session

from models.models import TaskTable
from schemas.schemas import TaskCreate, TaskUpdate
from repository.repository import TaskRepo
from exceptions.exceptions import NotFoundError, ValidationError
from responses.responses import build_success_response

VALID_STATUSES = {
    "pending", 
    "in-progress", 
    "done"
}

VALID_PRIORITIES = {
    "low", 
    "medium", 
    "high"
}

VALID_SORTINGS = {
    "due_date", 
    "created_at", 
    "updated_at",
    "completed_at"
}


def create_task(
    task: TaskCreate, 
    db: Session
):

    new_task = TaskTable(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        due_date=task.due_date,
        tags=task.tags,
        created_at=datetime.now(),
    )

    TaskRepo.create_task(new_task, db)

    return build_success_response("Task created successfully", new_task)


def get_tasks(
    status: str | None,
    priority: str | None,
    sort: str | None,
    page: int,
    limit: int,
    db: Session
):

    if page < 1:
        page = 1
    if limit < 1:
        limit = 10
    if limit > 100:
        limit = 100

    if status is not None and status not in VALID_STATUSES:
        raise ValidationError("Invalid status filter. Valid options are: pending, in-progress and done.")
    if priority is not None and priority not in VALID_PRIORITIES:
        raise ValidationError("Invalid priority filter. Valid options are: low, medium and high.")
    if sort is not None and sort not in VALID_SORTINGS:
        raise ValidationError("Invalid sorting filter. Valid options are: due_date, created_at, updated_at and completed_at.")
    
    total_tasks = TaskRepo.get_tasks_count(db)
    tasks = TaskRepo.get_tasks(status, priority, sort, page, limit, db)

    extra_meta = {
        "total tasks": total_tasks,
        "status filter": status,
        "priority filter": priority,
        "sorting by": sort,
        "page": page,
        "limit": limit,
        "total matching tasks": len(tasks)
    }

    return build_success_response("Tasks retrieved successfully", tasks, extra_meta)


def get_task_by_id(
    id: int,
    db: Session
):

    task = TaskRepo.get_task_by_id(id, db)
    if task is None:
        raise NotFoundError("Task not found")
    
    return build_success_response("Task retrieved successfully", task)


def update_task(
    id: int,
    task: TaskUpdate,
    db: Session
):

    existing_task = TaskRepo.get_task_by_id(id, db)
    if existing_task is None:
        raise NotFoundError("Task not found")

    for field, value in task.model_dump(exclude_unset=True).items():
        if field == "status" and value == "done":
            existing_task.completed_at = datetime.now()

        setattr(existing_task, field, value)

    updated_task = TaskRepo.update_task(existing_task, db)

    return build_success_response("Task updated successfully", updated_task)

def delete_task(
    id: int,
    db: Session
):

    task = TaskRepo.get_task_by_id(id, db)
    if task is None:
        raise NotFoundError("Task not found")

    TaskRepo.delete_task(task, db)