import json
from typing import Union, List
from sqlalchemy import or_, true, false

from todoapp.models.task import Task
from todoapp.dto.task import TaskDTO, TaskPatchDTO


class TaskRepository():
    def __init__(self, db):
        """

        :param db:
        """
        self.db = db

    def create(self, task: TaskDTO) -> int:
        """
        param task: Task to be created
        return: ID of the created task
        """
        task = Task(title=task.title, description=task.description)
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except:
            self.db.rollback()
        return task.id

    def get(self, task_id: int) -> Union[Task, None]:
        """
        :param task_id: ID of the task to be retrieved
        :return: Task with task_id as ID
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            return task
        return None

    def get_by_title(self, title: str) -> Union[Task, None]:
        """
        :param title: title of the task to be retrieved
        :return: Task with given title
        """
        task = self.db.query(Task).filter(Task.title == title).first()
        if task:
            return task
        return None

    def get_all(self) -> Union[List[Task], None]:
        """
        :return: All tasks in DB
        """
        tasks = self.db.query(Task).all()
        if len(tasks):
            return tasks
        return None

    def update(self, task_id: int, task_dto: TaskPatchDTO) -> Union[Task, None]:
        """
        :param task_id: ID of the task to be updated
        :param task_dto: Structure with new values of task
        :return: ID of the updated task
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            if task_dto.title:
                task.title = task_dto.title
            if task_dto.description:
                task.description = task_dto.description
            if task_dto.completed is True:
                task.completed = task_dto.completed
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
            return task.id
        else:
            return None

    def delete(self, task_id: int) -> None:
        """
        :param task_id: ID of the task to be deleted
        :return: ID of the deleted task
        """
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            try:
                self.db.delete(task)
                self.db.commit()
            except:
                self.db.rollback()

    def search(self, qlist: List[str]):
        """
        :param qlist: List of the search terms
        :return: Tasks containing above terms in the description
        """
        conditions = [Task.description.contains(q) for q in qlist]
        tasks = self.db.query(Task).filter(or_(i for i in conditions)).all()
        return tasks
