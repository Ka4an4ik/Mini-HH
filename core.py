from database import sync_engine, Base
from sqlalchemy import text, insert, select, update
from models import metadata, workers_table
import json

def select_func():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 'HIIIII'"))
        print(f"{res}") 
        print(res.fetchone())  

def create_tables():
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)

def print_hi():
    with sync_engine.connect() as printer:
        result = printer.execute(text("SELECT 'Hiiiiii'"))
        print(f"{result.fetchone()}")  

def insert_values():
    with sync_engine.connect() as insert:
        insert.execute(text("INSERT INTO workers (username) VALUES ('Denis'), ('Denis2'), ('Denis3')"))
        insert.commit()  


def insert_via_function():
    with sync_engine.connect() as ins_func:
        res = insert(workers_table).values(
            [
                {"username" : "Denis4"},
                {"username" : "Denis5"}
            ]
        )
        ins_func.execute(res)
        ins_func.commit()






def show_result():
    with sync_engine.begin() as result:
        res = result.execute(text("SELECT * FROM workers"))

        print(res.fetchall())

        # columns = res.keys()
        # data = [dict(zip(columns, row)) for row in res.fetchall()]
        # json_data = json.dumps(data, ensure_ascii=False, indent=4)
        # print(f'result = {json_data}')


def select_workers():
    
    with sync_engine.connect() as conn:
        query = select(workers_table)
        result = conn.execute(query)
        workers = result.all()
        print(f"{workers}")


def update_worker(worker_id : int = 2, new_username : str = "Misha"):
    with sync_engine.connect() as conn:
        # stmt = text("UPDATE workers SET username=:username WHERE id=:id")
        # stmt = stmt.bindparams(username = new_username, id = worker_id)

        stmt = update(workers_table).values(username = new_username).filter_by(id = worker_id)
        conn.execute(stmt)
        conn.commit()