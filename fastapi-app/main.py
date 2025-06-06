from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import settings
from core.models import db_helper

from api import router as api_router

@asynccontextmanager
async def lifespan(app):
    yield
    await db_helper.dispose()

main_app = FastAPI(lifespan= lifespan)
main_app.add_middleware(CORSMiddleware,
        allow_origins= settings.cors_data.allowed_origins,
        allow_methods= ['*'],
        allow_headers= ['*'],
        allow_credentials=True)
main_app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("main:main_app", reload = True, 
                host=settings.run.host, 
                port=settings.run.port)