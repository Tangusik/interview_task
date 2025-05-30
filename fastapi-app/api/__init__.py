from fastapi import APIRouter
from core.config import settings
from .tasks import router as task_router


router = APIRouter()
router.include_router(task_router)