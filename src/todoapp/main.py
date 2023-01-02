from fastapi import FastAPI

from todoapp.routers import task
from todoapp.config.database import create_tables

create_tables()
app = FastAPI()
app.include_router(task.router)


@app.get("/")
async def root():
    return {"message": "Welcome to todo list application"}