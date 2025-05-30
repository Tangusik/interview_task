from typing import Annotated
from fastapi import APIRouter, Depends
from crud.tasks import get_all_tasks, create_task, delete_task, patch_task
from core.schemas.tasks import TaskCreate, TaskPatch, TaskRead
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(tags=['Tasks'], prefix="/tasks")

@router.get("", response_model=list[TaskRead])
async def get_tasks(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    tasks = await get_all_tasks(session=session)
    return tasks

@router.post("", response_model=TaskRead)
async def task_create(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_create: TaskCreate):
    task = await create_task(session=session, task_create=task_create)
    return task

@router.delete("/{task_id}")
async def task_delete(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_id:int):
    await delete_task(session=session, task_id= task_id)
    return None

@router.patch("/{task_id}")
async def task_patch(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_patch:TaskPatch, task_id:int):
    task = await patch_task(session=session, task_patch= task_patch, task_id=task_id)
    return task