import pymysql

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'user',
    'db': 'rk6_schema'
}

'''connection = pymysql.connect(
    host=db_config['host'],
    port=db_config['port'],
    user=db_config['user'],
    password=db_config['password'],
    db=db_config['db']
)'''

def select(sql_statement, config):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    schema = [i[0] for i in cursor.description]
    output = [dict(zip(schema, row)) for row in result]
    cursor.close()
    connection.close()
    return output

res = select('SELECT * from account', db_config)
print(res)