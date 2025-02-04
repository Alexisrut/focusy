from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession

from models import init_db, Task, async_session
import requests as rq

async def import_tasks_from_excel(session):
    df = pd.read_excel('task_9.xlsx')
    
    df['task_explain'] = df['task_explain'].fillna('').astype(str)

    for _, row in df.iterrows():
        task = Task(
            task_id=row['task_id'],
            task_name=row['task_name'],
            task_category=row['task_category'],
            task_word=row['task_word'],
            task_correct=row['task_correct'],
            task_incorrect=row['task_incorrect'],
            task_explain=row['task_explain']
        )
        session.add(task)
    
    await session.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print('Bot is ready')
    async with async_session() as session:
        await import_tasks_from_excel(session)  # Add await here
    yield   



app = FastAPI(title = "Focusy", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Кол-во выполненных всего
@app.get("/api/all_completed/{tg_id}")
async def all_completed(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_completed_tasks_count(user)
    return completed_tasks_count

#Кол-во выполненных по теме
@app.get("/api/theme_completed/{tg_id}/{theme}")
async def theme_completed(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_theme_completed_tasks_count(user, theme)
    return completed_tasks_count

#Получение xp + coins - готово
@app.get("/api/stats/{tg_id}")
async def stats(tg_id: int):
    print('get_stats')
    user_id = await rq.add_user(tg_id)
    stats = await rq.get_stats(user_id)
    return stats

#Изменение xp + coins - готово
@app.post("/api/change_coins/{tg_id}/{amount}")
async def change_coins(tg_id: int, amount: str):
    print('add_coins')
    user_id = await rq.add_user(tg_id)
    coins = int(amount)
    await rq.change_coins(user_id, coins)

@app.post("/api/change_xp/{tg_id}/{amount}")
async def change_xp(tg_id: int, amount: str):
    print('add_xp')
    user_id = await rq.add_user(tg_id)
    xp = int(amount)
    await rq.change_xp(user_id, xp)

#Получение невыполненных заданий по теме - готово
@app.get("/api/incomplete-tasks/{tg_id}/{theme}")
async def incomplete_task(tg_id: int):
    print('get_incomplete')
    user_id = await rq.get_user(tg_id)
    tasks = await rq.get_incomplete_tasks(user_id, theme)
    print(tasks)
    return tasks

#Получение тем по предмету - готово
@app.get("/api/theme-tasks/{tg_id}")
async def theme_task(tg_id: int):
    print('get_theme')
    user_id = await rq.get_user(tg_id)
    tasks = await rq.get_theme(user_id)
    print(tasks)
    return tasks

#Измение готовности - готово
@app.post("/api/mark_complete/{tg_id}/{task_id}")
async def mark_complete_task(tg_id, task_id):
    tg_id = int(tg_id)
    task_id = int(task_id)
    user_id = await rq.get_user(tg_id)
    print(f'Userererere: {user_id}, {task_id}')
    await rq.mark_task_completed(user_id, task_id)

#Все задания в неготовые - готово
@app.post("/api/full_to_incomplete/{tg_id}/{theme}")
async def full_to_incomplete(tg_id, theme):
    tg_id = int(tg_id)
    user_id = await rq.get_user(tg_id)
    await rq.mark_theme_incompleted(user_id, theme)