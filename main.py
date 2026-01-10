from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.v1.api import api_router
from db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (se necessário)

app = FastAPI(title="API FastAPI Completa", lifespan=lifespan)

app.include_router(api_router)
