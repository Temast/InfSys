from flask import Blueprint, request, render_template

import os

from sql_provider import SQLProvider

auth_blueprint = Blueprint(
    'auth_blueprint',
    __name__,
    template_folder='templates'
)
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@auth_blueprint.route('/', methods=['GET', 'POST'])
def auth_handler():
    if request.method == 'GET':
        return render_template('input_login.html')
    else:
        #
        login = request.form.get('login', '')
        password = request.form.get('password', '')
        sql = provider.get(
            'internal_user.sql',
            {
                'login': login,
                'password': password
            }
        )
        return sql
