from sqlalchemy import Integer, and_, select, func, cast
from models import WorkersORM, ResumesORM, Workload
from database import session_factory, sync_engine, Base

# создание моделей с помощью сессии и декларативного метода
def insert_data():
    worker_one = WorkersORM(username = 'Denis ORM')
    worker_two = WorkersORM(username = 'Denis ORM2')
    with session_factory() as session:
        session.add(worker_one)
        session.add(worker_two)
        session.commit()

def create_table_via_orm():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

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

def insert_resumes():
    with session_factory() as session:
        res1 = ResumesORM(title = "Python dev", compensation = 40000, workload = Workload.fulltime, worker_id = 1)
        res2 = ResumesORM(title = "Python scince", compensation = 60000, workload = Workload.parttime, worker_id = 2)
        res3 = ResumesORM(title = "Python middle", compensation = 80000, workload = Workload.fulltime, worker_id = 3)

        session.add_all([res1, res2, res3])
        session.commit()
        


def select_resumes(like_language : str = "Python"):
    with session_factory() as session:
        """
        select workload, avg(compensation)::int as avg_compensation
        from resumes
        where title like "%Python%" and compensation > 40000
        group by workload
        """

        query = select(ResumesORM.workload, 
                       cast(func.avg(ResumesORM.compensation), Integer).label("avg_compensation")
        ).filter(and_(
            ResumesORM.title.contains(like_language),
            ResumesORM.compensation > 40000,
        )).group_by(ResumesORM.workload)
        # print(query.compile(compile_kwargs={"literal_binds": True}))

        result = session.execute(query).all()
        print(result)

