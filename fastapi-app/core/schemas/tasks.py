
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    completed: bool

class TaskRead(TaskBase):
    id:int

class TaskCreate(TaskBase):
    pass

class TaskPatch(BaseModel):
    completed: bool
