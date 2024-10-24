from flask import requset, session

def auth_user(request, provider):
    login = request.form.get('login', '')
    password = request.form.get('password', '')
    sql = provider.get(
        'internal_user.sql',
        {
            'login': login,
            'password': password
        }
    )
    user = find_user(sql, {})
    session['user_id'] = user['user_id']
    session['user_group'] = user['user_group']
    session.permanent = True
    return {
        'status': 'OK',
        'message': 'Successful'
    }


def find_user(sql, db_config):
    return{
        'user_id': 1,
        'user_group': 'typical'
    }