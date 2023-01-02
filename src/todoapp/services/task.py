from typing import List

from todoapp.dto.task import TaskDTO, TaskPatchDTO
from todoapp.services.base import DBSessionContext
from todoapp.utils.app_exceptions import AppException
from todoapp.utils.service_result import ServiceResult
from todoapp.dto.task import TaskResponseDTO
from todoapp.repository.tasks import TaskRepository


class TaskService(DBSessionContext):
    def create(self, task: TaskDTO) -> ServiceResult:
        """
        param task: Task to be created
        return: ID of the created task
        """
        task_id = TaskRepository(self.db).create(task)
        if not task_id:
            return ServiceResult(AppException.TaskCreateItem(), status_code=422)
        return ServiceResult(TaskResponseDTO(task_id=task_id), status_code=200)

    def get(self, task_id: int) -> ServiceResult:
        """
        :param task_id: ID of the task to be retrieved
        :return: Task with task_id as ID
        """
        task = TaskRepository(self.db).get(task_id)
        if not task:
            return ServiceResult(AppException.TaskGetItem({"task_id": task_id}), status_code=404)
        return ServiceResult(TaskDTO(title=task.title, description=task.description, completed=task.completed), status_code=200)

    def get_by_title(self, title: str) -> ServiceResult:
        """
        :param title: title of the task to be retrieved
        :return: Task with given title
        """
        task = TaskRepository(self.db).get_by_title(title)
        if not task:
            return ServiceResult(AppException.TaskGetItem({"title": title}),  status_code=404)
        return ServiceResult(TaskDTO(title=task.title, description=task.description, completed=task.completed), status_code=200)

    def get_all(self) -> ServiceResult:
        """
        :return: All tasks in DB
        """
        tasks = TaskRepository(self.db).get_all()
        if not tasks:
            return ServiceResult(AppException.TaskGetAllItems(), status_code=404)
        return ServiceResult(tasks, status_code=200)

    def update(self, task_id: int, task: TaskPatchDTO) -> ServiceResult:
        """
        :param task_id: ID of the task to be updated
        :param task: Structure with new values of task
        :return: ID of the updated task
        """
        task_id = TaskRepository(self.db).update(task_id, task)
        if not task_id:
            return ServiceResult(AppException.TaskGetItem({"task_id": task_id}), status_code=404)
        return ServiceResult(TaskResponseDTO(task_id=task_id), status_code=200)

    def delete(self, task_id: int) -> ServiceResult:
        """
        :param task_id: ID of the task to be deleted
        :return: ID of the deleted task
        """
        TaskRepository(self.db).delete(task_id)
        return ServiceResult(TaskResponseDTO(task_id=task_id), status_code=204)

    def search(self, q: List[str]) -> ServiceResult:
        """
        :param q: List of the search terms
        :return: Tasks containing above terms in the description
        """
        tasks = TaskRepository(self.db).search(q)
        if not tasks:
            return ServiceResult(AppException.TaskGetAllItems(),  status_code=404)
        return ServiceResult(tasks, status_code=200)
