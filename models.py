import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import enum

metadata = MetaData()

# создание таблицы декларативным методом

class WorkersORM(Base):
    __tablename__ = "workers"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str]
    


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"



class ResumesORM(Base):
    __tablename__ = "resumes"

    id : Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id : Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at : Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))



# создание таблицы интерактивным методом 
workers_table = Table(
    "workers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)

