from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.tasks import Task
from core.schemas.tasks import TaskCreate, TaskPatch


async def get_all_tasks(session: AsyncSession) -> Sequence[Task]:
    req = select(Task).order_by(Task.id)
    res = await session.scalars(req)
    return res.all()

async def create_task(session: AsyncSession, task_create: TaskCreate) -> Task:
    task = Task(**task_create.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

async def delete_task(session: AsyncSession, task_id: int) -> None:
    task  = await session.get(Task, task_id)
    await session.delete(task)
    await session.commit()
    return None

async def patch_task(session: AsyncSession, task_patch:TaskPatch, task_id: int) -> Task:
    task = await session.get(Task, task_id)
    task.completed = task_patch.completed
    await session.commit()
    await session.refresh(task)
    return task