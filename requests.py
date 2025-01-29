from sqlalchemy import select, update, delete, func
from models import async_session, User, Themes
from pydantic import BaseModel, ConfigDict
from typing import List

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
    
class ThemeSchema(BaseModel):
    id: int
    theme: str
    completed: int
    max_score: int
    user: int

    model_config = ConfigDict(from_attributes = True)


async def get_theme(user_id):
    async with async_session() as session:
        themes = await session.scalars(select(Themes).where(Themes.user == user_id))

        serialized_themes = [ThemeSchema.model_validate(theme) for theme in themes]

        return serialized_themes
    
async def get_completed_tasks_count(user_id):
    async with async_session() as session:
        completed_tasks_count = await session.scalar(select(func.count(Themes.id)).where(Themes.completed == Themes.max_score))
        return completed_tasks_count