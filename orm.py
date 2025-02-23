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