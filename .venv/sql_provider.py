import os
from string import Template


class SQLProvider:

    def __init__(self, path):
        self._scripts = {}
        for file in os.listdir(path):
            self._scripts[file] = Template(open(f'{path}/{file}', 'r').read())

    def get(self, name, params):
        if name not in self._scripts:
            raise ValueError('No such file in sql_provider')
        return self._scripts[name].substitute(**params)

if __name__ == '__main__':
    sql_provider = SQLProvider('auth/sql')
    sql_statement = sql_provider.get(
        'internal_user.sql',
        dict(login='user_typical', password='password_typical')
    )
    print(sql_statement)