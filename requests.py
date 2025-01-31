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

async def add_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            return user.id
        user = User(tg_id = tg_id)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user.id

async def get_completed_tasks_count(user_id: int) -> int:
    """Get count of completed tasks for specific user"""
    async with async_session() as session:
        result = await session.scalar(
            select(func.count(UserTask.id))
            .where(UserTask.user_id == user_id)
            .where(UserTask.completed == True)
        )
        return result or 0

async def get_incomplete_tasks(user_id: int) -> list[Task]:
    """Get list of incomplete tasks for specific user"""
    async with async_session() as session:
        result = await session.scalars(
            select(Task)
            .join(UserTask, Task.id == UserTask.task_id)
            .where(UserTask.user_id == user_id)
            .where(UserTask.completed == False)
        )
        serialized_tasks = [
            TaskSchema.model_validate(t).model_dump() for t in result
        ]
        return serialized_tasks

async def get_or_create_user_task(user_id: int, task_id: int) -> UserTask:
    """Get or create UserTask relationship for a user and task"""
    async with async_session() as session:
        # Try to get existing UserTask
        user_task = await session.scalar(
            select(UserTask)
            .where(UserTask.user_id == user_id)
            .where(UserTask.task_id == task_id)
        )
        
        if not user_task:
            # Create new relationship if doesn't exist
            user_task = UserTask(
                user_id=user_id,
                task_id=task_id,
                completed=False
            )
            session.add(user_task)
            await session.commit()
            await session.refresh(user_task)
            
        return user_task

async def mark_task_completed(user_id: int, task_id: int):
    """Mark specific task as completed for user"""
    async with async_session() as session:
        user_task = await get_or_create_user_task(user_id, task_id)
        user_task.completed = True
        await session.commit()