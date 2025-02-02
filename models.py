from sqlalchemy import ForeignKey, Column, BigInteger, String, DateTime, Boolean, Integer
from typing import List
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from datetime import datetime

engine = create_async_engine(
    "sqlite+aiosqlite:///./focusy.db?charset=utf8",
    connect_args={"check_same_thread": False},
    echo=True
)
#engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True)
    tg_id = mapped_column(BigInteger)

class UserTask(Base):
    __tablename__ = 'user_tasks'  # Промежуточная таблица (M2M)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_info.id'))
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    completed: Mapped[bool] = mapped_column(Boolean, default=False) 

    user: Mapped["UserInfo"] = relationship(back_populates="completed_tasks")
    task: Mapped["Task"] = relationship(back_populates="completed_by")

class UserInfo(Base):
    __tablename__ = 'user_info'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(64))
    year: Mapped[int] = mapped_column(Integer)
    coins: Mapped[int] = mapped_column(default=0)
    xp: Mapped[int] = mapped_column(default=0)
    subscription: Mapped[bool] = mapped_column(default=False)
    time_of_subscription: Mapped[int] = mapped_column(BigInteger, default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

    completed_tasks: Mapped[list["UserTask"]] = relationship(
        back_populates="user", 
        cascade="all, delete-orphan"
    )

class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[str] = mapped_column(String(64))
    task_name: Mapped[str] = mapped_column(String(64))  # Changed from int to str
    task_category: Mapped[str] = mapped_column(String(256))
    task_word: Mapped[str] = mapped_column(String(256))  # Changed from bool to str
    task_correct: Mapped[str] = mapped_column(String(16))  # Changed from bool to str
    task_incorrect: Mapped[str] = mapped_column(String(16))  # Changed from bool to str
    task_explain: Mapped[str] = mapped_column(String(512), nullable=False)

    completed_by: Mapped[list["UserTask"]] = relationship(
        back_populates="task", 
        cascade="all, delete-orphan"
    )




async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drop existing tables
        await conn.run_sync(Base.metadata.create_all)