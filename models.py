from sqlalchemy import ForeignKey, Column, BigInteger, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from datetime import datetime

engine = create_async_engine('sqlite+aiosqlite:///focusy.db', echo=True)
#engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True)
    tg_id = mapped_column(BigInteger)


class UserInfo(Base):
    __tablename__ = 'user_info'

    id: Mapped[int] = mapped_column(primary_key=True)
    coins: Mapped[int] = mapped_column(default=0)
    xp: Mapped[int] = mapped_column(default=0)
    subscription: Mapped[bool] = mapped_column(default=False)
    time_of_subscription: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

    tasks_completed = relationship("UserTask", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    # Add columns from your Excel file here. Example:
    task_id: Mapped[str] = mapped_column(String(64))
    task_name: Mapped[int] = mapped_column(String(64))
    task_category: Mapped[str] = mapped_column(String(256))
    task_word: Mapped[bool] = mapped_column(String(256))
    task_correct: Mapped[bool] = mapped_column(String(16))
    task_incorrect: Mapped[bool] = mapped_column(String(16))
    task_explain: Mapped[bool] = mapped_column(String(512))

    completed_by_users = relationship("UserTask", back_populates="task")


class UserTask(Base):
    __tablename__ = 'user_tasks'  # Промежуточная таблица (M2M)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id', ondelete="CASCADE"))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)  # Время выполнения

    user = relationship("User", back_populates="tasks_completed")
    task = relationship("Task", back_populates="completed_by_users")

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)