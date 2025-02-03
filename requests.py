from sqlalchemy import select, update, delete, func
from models import async_session, User, Task, UserInfo, UserTask
from pydantic import BaseModel, ConfigDict
from typing import List

class TaskSchema(BaseModel):
    id: int
    # Add columns from your Excel file here. Example:
    task_id: str
    task_name: str
    task_category: str
    task_word: str
    task_correct: str
    task_incorrect: str
    task_explain: str
    
    model_config = ConfigDict(from_attributes=True)

class StatsSchema(BaseModel):
    id: int
    # Add columns from your Excel file here. Example:
    tg_id: str
    coins: int
    xp: int
    
    model_config = ConfigDict(from_attributes=True)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def add_user_tasks(user_id: int, session: AsyncSession):
    # Create a new use

    # Fetch all existing tasks
    result = await session.execute(select(Task))
    tasks = result.scalars().all()

    # Create UserTask entries for each task
    for task in tasks:
        user_task = UserTask(user_id=user_id, task_id=task.id)
        session.add(user_task)

async def add_task_users(task_id: int, session: AsyncSession):
        # Fetch the task to ensure it exists
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    
    if not task:
        raise ValueError("Task not found")

    # Fetch all existing users
    result = await session.execute(select(User))
    users = result.scalars().all()

    # Create UserTask entries for each user
    for user in users:
        user_task = UserTask(user_id=user.id, task_id=task.id)
        session.add(user_task)

async def get_user(tg_id):
    async with async_session() as session:
        tg_id = int(tg_id)
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user != None:
            return user.id

async def add_user(tg_id, name, year):
    async with async_session() as session:
        print(tg_id)
        tg_id = int(tg_id)
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user != None:
            return user.id
        new_user = User(tg_id = tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        registered_user = await session.scalar(select(User).where(User.tg_id == tg_id))
        new_user_info = UserInfo(
            tg_id = tg_id, 
            name = name,
            year = int(year),
            user_id = registered_user.id,
            coins = 0,
            xp = 0,
            subscription = 0,
            time_of_subscription = 0
            )
        session.add(new_user_info)
        await session.commit()
        await session.refresh(new_user_info)
        await add_user_tasks(new_user.id, session)
        await session.commit()
        return new_user.id

async def get_completed_tasks_count(user_id: int) -> int:
    """Get count of completed tasks for specific user"""
    async with async_session() as session:
        result = await session.scalar(
            select(func.count(UserTask.id))
            .where(UserTask.user_id == user_id)
            .where(UserTask.completed == True)
        )
        return result or 0

async def get_theme_completed_tasks_count(user_id: int, theme: str) -> int:
    """Get count of completed tasks for specific user"""
    async with async_session() as session:
        result = await session.scalar(
            select(func.count(UserTask.id))
            .join(UserTask, Task.id == UserTask.task_id)
            .where(UserTask.theme == theme)
            .where(UserTask.user_id == user_id)
        )
        return result or 0


async def get_incomplete_tasks(user_id: int, theme: str) -> list[Task]:
    """Get list of incomplete tasks for specific user"""
    async with async_session() as session:
        result = await session.scalars(
            select(Task)
            .join(UserTask, Task.id == UserTask.task_id)
            .where(Task.task_name == theme)
            .where(UserTask.user_id == user_id)
            .where(UserTask.completed == False)
        )
        serialized_tasks = [
            TaskSchema.model_validate(t).model_dump() for t in result
        ]
        return serialized_tasks

async def get_stats(user_id: int):
    async with async_session() as session:
        result = await session.scalars(
            select(UserInfo).where(UserInfo.user_id == user_id)
        )
        serialized_tasks = [
            StatsSchema.model_validate(t).model_dump() for t in result
        ]
        return serialized_tasks

async def get_theme(user_id: int):
    async with async_session() as session:
        result = await session.scalars(
            select(func.distinct(Task.task_name))
        )
        unique_names = [name for name in result]
        return unique_names

async def change_coins(user_id: int, coins: int):
    async with async_session() as session:
        result = await session.scalars(
            select(UserInfo).where(UserInfo.user_id == user_id)
        )
        result.coins += coins
        await session.commit()

async def change_xp(user_id: int, xp: int):
    async with async_session() as session:
        result = await session.scalars(
            select(UserInfo).where(UserInfo.user_id == user_id)
        )
        result.xp += xp
        await session.commit()
        


async def mark_task_completed(user_id: int, task_id: int):
    """Mark specific task as completed for user"""
    async with async_session() as session:
        user_task = await session.scalar(
            select(UserTask)
            .where(UserTask.user_id == user_id)
            .where(UserTask.task_id == task_id)
        )
        user_task.completed = True
        print(user_task.user_id, user_task.task_id)
        await session.commit()

async def mark_theme_incompleted(user_id: int, theme: str):
    async with async_session() as session:
        result = await session.scalars(
            select(Task)
            .join(UserTask, Task.id == UserTask.task_id)
            .where(Task.task_name == theme)
            .where(UserTask.user_id == user_id)
        )
        for i in result:
            i.completed = False
        await session.commit()