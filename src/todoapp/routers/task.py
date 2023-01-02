from typing import List, Union

from fastapi import APIRouter
from fastapi import Query
from pydantic import Required

from todoapp.dto.task import TaskDTO, TaskPatchDTO
from todoapp.services.task import TaskService
from todoapp.utils.service_result import ServiceResult

router = APIRouter(prefix="/tasks")
task_service = TaskService()


@router.post("/")
async def create(task: TaskDTO) -> ServiceResult:
    """
    :param task: Task to be created
    :return: ID of the created task
    """
    return task_service.create(task)


@router.get("")
async def get(task_id: Union[int, None] = None, title: Union[str, None] = None) -> ServiceResult:
    """
    :param title: Title of the task to be retrieved
    :param task_id: ID of the task to be retrieved
    :return: The required task (in case if title or ID is present), else return all tasks
    """
    if task_id:
        return task_service.get(task_id)
    if title:
        return task_service.get_by_title(title)
    return task_service.get_all()


@router.patch("/{task_id}")
async def update(task: TaskPatchDTO, task_id: int = Query(default=Required)) -> ServiceResult:
    """
    :param task_id: ID of the task to be updated
    :param task: Structure with new values of task
    :return: ID of the updated task
    """
    return task_service.update(task_id, task)


@router.delete("/{task_id}")
async def delete(task_id: int = Query(default=Required)) -> ServiceResult:
    """
    :param task_id: ID of the task to be deleted
    :return: ID of the deleted task
    """
    return task_service.delete(task_id)


@router.get("/search")
async def search(q: List[str] = Query(default=Required)) -> ServiceResult:
    """
    :param q: List of the search terms
    :return: Tasks containing above terms in the description
    """
    return task_service.search(q)
