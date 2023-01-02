from pydantic.class_validators import Optional
from pydantic.main import BaseModel
from fastapi import Query
from pydantic import Required


class TaskDTO(BaseModel):
    title: str = Query(default=Required, max_length=10)
    description: str = Query(default=Required)
    completed: Optional[bool]


class TaskPatchDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]


class TaskResponseDTO(BaseModel):
    task_id: int

    class Config:
        orm_mode = True
