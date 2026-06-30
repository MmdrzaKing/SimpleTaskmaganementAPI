from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from exceptions.exceptions import ConflictError, DatabaseError
from models.models import TaskTable


class TaskRepo:

    @staticmethod
    def create_task(new_task, db):
        try:
            db.add(new_task)
            db.commit()
            db.refresh(new_task)
        except IntegrityError as exc:
            db.rollback()
            raise ConflictError("Task could not be created due to a database constraint.") from exc
        except SQLAlchemyError as exc:
            db.rollback()
            raise DatabaseError("Database error while creating task.") from exc
        
    @staticmethod
    def get_tasks_count(db):
        try:
            total_tasks = db.query(TaskTable).count()
            return total_tasks

        except SQLAlchemyError as exc:
            raise DatabaseError("Database error while fetching tasks.") from exc

    @staticmethod
    def get_tasks(status, priority, sort, page, limit, db):
        try:
            query = db.query(TaskTable)

            if status is not None:
                query = query.filter(TaskTable.status == status)

            if priority is not None:
                query = query.filter(TaskTable.priority == priority)

            if sort is not None:
                if sort == "due_date":
                    query = query.order_by(TaskTable.due_date.desc())
                elif sort == "created_at":
                    query = query.order_by(TaskTable.created_at.desc())
                elif sort == "updated_at":
                    query = query.order_by(TaskTable.updated_at.desc())
                elif sort == "completed_at":
                    query = query.order_by(TaskTable.completed_at.desc())

            return query.offset((page - 1) * limit).limit(limit).all()
        
        except SQLAlchemyError as exc:
            raise DatabaseError("Database error while fetching tasks.") from exc

    @staticmethod
    def get_task_by_id(id, db):
        try:
            task = db.query(TaskTable).filter(TaskTable.id == id).first()
            return task
        except SQLAlchemyError as exc:
            raise DatabaseError("Database error while fetching task.") from exc

    @staticmethod
    def update_task(task, db):
        try:
            db.commit()
            db.refresh(task)
            return task
        except IntegrityError as exc:
            db.rollback()
            raise ConflictError("Task could not be updated due to a database constraint.") from exc
        except SQLAlchemyError as exc:
            db.rollback()
            raise DatabaseError("Database error while updating task.") from exc

    @staticmethod
    def delete_task(task, db):
        try:
            db.delete(task)
            db.commit()
        except IntegrityError as exc:
            db.rollback()
            raise ConflictError("Task could not be deleted due to a database constraint.") from exc
        except SQLAlchemyError as exc:
            db.rollback()
            raise DatabaseError("Database error while deleting task.") from exc