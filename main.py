from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession

from models import init_db, Task, async_session
import requests as rq

async def import_tasks_from_excel(session: AsyncSession):
    df = pd.read_excel('task_9.xlsx')
    
    for _, row in df.iterrows():
        task = Task(
            task_id = row['task_id'],
            task_name = row['task_name'],
            task_category = row['tsk_category'],
            task_word = row['task_word'],
            task_correct = row['task_correct'],
            task_incorrect = row['task_incorrect'],
            task_explain = row['task_explain']
        )
        session.add(task)
    
    await session.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print('Bot is ready')
    async with async_session() as session:
        import_tasks_from_excel(session)
    yield   



app = FastAPI(title = "Focusy", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/tasks/{tg_id}")
async def get_tasks(tg_id: int):
    user_id = await rq.add_user(tg_id)
    return await rq.get_theme(user_id)

@app.get("/api/main/{tg_id}")
async def profile(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_completed_tasks_count(user)
    return {"tg_id": tg_id, "completed_tasks_count": completed_tasks_count}

@app.get("/api/stats/{tg_id}")
async def stats(tg_id: int):
    user = await rq.add_user(tg_id)

@app.get("/api/incomplete-tasks/{tg_id}")
async def incomplete_task(tg_id: int):
    user_id = await rq.add_user(tg_id)
    tasks = await rq.get_incomplete_tasks(user_id)
    return tasks

@app.get("/api/mark_complete/{tg_id}/{task_id}")
async def mark_complete_task(tg_id, task_id):
    rq.mark_task_completed(tg_id, task_id)