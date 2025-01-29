from sqlalchemy import ForeignKey, Column, BigInteger, String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker

engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True)
    tg_id = mapped_column(BigInteger)


class Themes(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key = True)
    theme: Mapped[str] = mapped_column(String(128))
    completed: Mapped[int] = mapped_column(default = False)
    max_score: Mapped[int] = mapped_column(default = False)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'), ondelete = 'CASCADE')


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)