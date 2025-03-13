from sqlalchemy import select
from models import WorkersORM
from database import session_factory

# создание моделей с помощью сессии и декларативного метода
def insert_data():
    worker_one = WorkersORM(username = 'Denis ORM')
    worker_two = WorkersORM(username = 'Denis ORM2')
    with session_factory() as session:
        session.add(worker_one)
        session.add(worker_two)
        session.commit()

def select_data():
    with session_factory() as session:
        # worker_id = 1
        # worker_list = session.get(WorkersORM, worker_id)
        query = select(WorkersORM)
        result = session.execute(query)
        workers = result.scalars().all()
        print(f"{workers}")

def update_worker(worker_id : int = 2, new_username : str = "Misha"):
    with session_factory() as session:
        worker_michael = session.get(WorkersORM, worker_id)
        worker_michael.username = new_username
        session.commit()