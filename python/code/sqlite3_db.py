# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-03-15 17:44:50
# @FileName: sqlite3_db

import os
import sys
import sqlite3

DB_NAME = "sqlite.db"
SCHEMA_FILENAME = "sqlite.schema.sql"

INSERT_SQL = """
  insert into project (name, description, deadline)  
  values ('test_sqlite', 'test sqlite', '2020-03-31');

  insert into task(details, status, deadline, project)
  values('select', 'done', '2020-03-15', 'test_sqlite');

  insert into task(details, status, deadline, project)
  values('delete', 'waiting', '2020-03-25', 'test_sqlite');

  insert into task(details, status, deadline, project)
  values('update', 'activate', '2020-03-20', 'test_sqlite');

"""

def create_db():
    db_is_new = not os.path.exists(DB_NAME)
    with sqlite3.connect(DB_NAME) as conn:
        if db_is_new:
            print ("Creating ....")
            with open(SCHEMA_FILENAME, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)

            print ("Inserting data ...")
            
            conn.executescript(INSERT_SQL)
        else:
            print ("DB exists, assume schema does, too.")


def query():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        select id, priority, details, status, deadline from task
        --where project = "test_sqlite"
        """)
        for row in cursor.fetchall():
            task_id, priority, details, status, deadline = row
            print (row)
            print ("{:2d} [{:d}] {:<10} [{:<8}] ({})".format(task_id, priority, details, status, deadline))


def query_metadata():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        select * from task where project = "test_sqlite"
        """)
        for col_info in cursor.description:
            print (col_info)

def query_row_objects():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql_str = """
            select name, description, deadline from project
            where name = "test_sqlite"
        """
        cursor.execute(sql_str)
        name, description, deadline = cursor.fetchone()
        print ("Project details for {} {} \n due {}".format(name, description, deadline))

        sql_str = """
            select * from task where project = "test_sqlite" order by deadline
        """
        cursor.execute(sql_str)
        print ("Next 5 tasks: ")
        for row in cursor.fetchmany(5):
            print ("{:2d} [{:<8}] ({})".format(row['id'], row['status'], row['deadline']))

def query_with_varibales():
    project_name = "test_sqlite"
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql_str = """
            select id, status, deadline from task 
            where project = ?
        """
        cursor.execute(sql_str, (project_name,))
        for row in cursor.fetchall():
            task_id, status, deadline = row
            print ("{:2d} [{:<8}] ({})".format(task_id, status, deadline))

def load_bulk():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        sql_str = """
            insert into task (priority, status, project)
            values (:priority, 'active', :project)
        """
        data = [
            {"priority" : 4, "project": "load_bulk"},
            {"priority" : 3, "project": "load_bulk"},
            {"priority" : 2, "project": "load_bulk"},
            {"priority" : 1, "project": "load_bulk"},
        ]
        cursor.executemany(sql_str, data)

class MyObj: 
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "Class MyObj({!r})".format(self.arg)

def define_col_type():


    def adapter_func(obj):
        import json
        import pickle
        print ("adapter_func({}) \n".format(obj))
        return pickle.dumps(obj)

    def converter_func(data):
        import json
        import pickle
        print ("converter_func({})".format(data))
        return pickle.loads(data)


    sqlite3.register_adapter(MyObj, adapter_func)
    sqlite3.register_converter("MyObj", converter_func)
    data_list = [
        #("aaa",),
        (MyObj("test define new column type"),),
        # (MyObj("43"),),
    ]

    with sqlite3.connect(DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        sql_create_str = """
            create table if not exists obj (
                id integer primary key autoincrement not null, 
                data MyObj 
            )
        """
        conn.execute(sql_create_str)
        cursor = conn.cursor()
        cursor.executemany("insert into obj (data) values (?)", data_list)

        cursor.execute("select id, data from obj")
        for obj_id, obj in cursor.fetchall():
            print (obj_id, obj)

def use_python_func():
    import codecs
    def encrypt(s):
        print ("Encrypting {!r}".format(s))
        return codecs.encode(s, 'rot-13')

    def decrypt(s):
        print ("Decrypting {!r}".format(s))
        return codecs.decode(s, 'rot-13')

    def show():
        cursor.execute("select id, details from task where project = 'test_sqlite'")
        for row in cursor.fetchall():
            print (row)

    with sqlite3.connect(DB_NAME) as conn:
        conn.create_function('encrypt', 1, encrypt)
        conn.create_function('decrypt', 1, decrypt)
        cursor = conn.cursor()

        print ("Original values ....")
        show()

        print ("Encrypting...")
        cursor.execute("update task set details=encrypt(details) where project='test_sqlite'")

        print ("Raw encrypt values...")
        show()

        print ("Decrypting in query....")
        cursor.execute("select id, decrypt(details) from task where project = 'test_sqlite'")
        for row in cursor.fetchall():
            print (row)

        print ("Decrypting...")
        cursor.execute("update task set details=decrypt(details) where project='test_sqlite'")
        

def transaction_commit():
    def show(conn_1):
        cursor = conn_1.cursor()
        cursor.execute("select name from project")
        for name in cursor.fetchall():
            print ("    ", name)
        
    with sqlite3.connect(DB_NAME) as conn_1:
        print ("Before changes: ")
        show(conn_1)
        cursor_1 = conn_1.cursor()
        cursor_1.execute("""
        insert into project(name, description, deadline) 
        values ("transaction_2", "transaction commit", "2020-03-31")
        """)

        print ("After changes in conn_1")
        show(conn_1)

        print ("Before commit")
        with sqlite3.connect(DB_NAME) as conn_2:
            show(conn_2)

        conn_1.commit()

        print ("After commit")
        with sqlite3.connect(DB_NAME) as conn_3:
            show(conn_3)

def transaction_rollback():
    def show(conn_1):
        cursor = conn_1.cursor()
        cursor.execute("select name from project")
        for name in cursor.fetchall():
            print ("    ", name)
        
    with sqlite3.connect(DB_NAME) as conn_1:
        print ("Before changes: ")
        show(conn_1)
        try:
            cursor = conn_1.cursor()
            cursor.execute("""delete from project where name = "test_sqlite" """)
            print ("After delete")
            show(conn_1)
            raise RuntimeError("simulated error")
        except Exception as err:
            print ("ERROR:", err)
            conn_1.rollback()
        else:
            conn_1.commit()
        print ("After changes: ")
        show(conn_1)


def locking_mode():
    import logging
    import threading
    import time


    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s (%(threadName)-10s) %(message)s'
    )

    isolation_level = sys.argv[1] #DEFERRED、IMMEDIATE、EXCLUSIVE

    def writer():
        with sqlite3.connect(DB_NAME, isolation_level=isolation_level) as conn:
            cursor = conn.cursor()
            cursor.execute("update task set priority = priority + 1")
            logging.debug("waiting to synchronize")
            ready.wait()
            logging.debug("PAUSING")
            time.sleep(1)
            conn.commit()
            logging.debug("CHANGES COMMITTED")

    def reader():
        with sqlite3.connect(DB_NAME, isolation_level=isolation_level) as conn:
            cursor = conn.cursor()
            logging.debug("waiting to synchronize")
            ready.wait()
            logging.debug("waiting over")
            cursor.execute("select * from task")
            logging.debug("SELECT EXECUTED")
            cursor.fetchall()
            logging.debug("results fetched")
    ready = threading.Event()
    threads = [
        threading.Thread(name="Reader 1", target=reader),
        threading.Thread(name="Reader 2", target=reader),
        threading.Thread(name="Writer 1", target=writer),
        threading.Thread(name="Writer 2", target=writer),
    ]
    [t.start() for t in threads]
    time.sleep(1)
    logging.debug("setting ready")
    ready.set()
    [t.join() for t in threads]

def sqlite3_db():
    """
    Args:
    Returns:
    Raises:
    """
    locking_mode()
    return
    transaction_rollback()
    return
    transaction_commit()
    return
    use_python_func()
    return
    define_col_type()
    return
    query()
    return
    load_bulk()
    return
    query_with_varibales()
    return
    query_row_objects()
    return
    query_metadata()
    return
    create_db()

if __name__ == "__main__":
    sqlite3_db()
