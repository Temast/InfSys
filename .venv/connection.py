import pymysql
from pymysql import OperationalError

class DBConnection:

    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**db_config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except (OperationalError, KeyError):
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.cursor:
            if exc_type:
                print(exc_type)
                print(exc_val)
                self.connection.rollback() # откат изменений БД
            else:
                self.connection.commit() # сохранение изменений БД
            self.cursor.close()
            self.connection.close()
        else:
            if exc_type:
                print(exc_type)
                print(exc_val)
        return True # чтобы в консоль не выводился traceback


db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'user',
    'db': 'rk6_schema'
}
sql_statement = 'SELECT * from account'

with DBConnection(db_config) as cursor:
    if cursor is None:
        raise ValueError('DB cursor is invalid')
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    schema = [i[0] for i in cursor.description]
    output = [dict(zip(schema, row)) for row in result]
    print(output)