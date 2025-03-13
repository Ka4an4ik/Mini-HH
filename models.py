import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from typing import Annotated, Optional
import enum

metadata = MetaData()


# Принцип DRY. Здесь мы можем воспроизвести повторяющийся код
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate= datetime.datetime.utcnow)]

# создание таблицы декларативным методом

class WorkersORM(Base):
    __tablename__ = "workers"
    id : Mapped[intpk]
    username : Mapped[str]
    


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"




class ResumesORM(Base):
    __tablename__ = "resumes"

    id : Mapped[intpk]
    title: Mapped[str] = mapped_column(String(50))
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id : Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at : Mapped[created_at]
    updated_at : Mapped[updated_at]



# создание таблицы интерактивным методом 
workers_table = Table(
    "workers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)

