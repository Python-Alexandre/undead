from fastapi import FastAPI
from api.v1.api import api_router
from db.init_db import init_db

app = FastAPI(title="API FastAPI Completa")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api_router)
