from flask import Flask, render_template

from auth.routes import auth_blueprint
from report.routes import report_blueprint
#from access import


app = Flask(__name__)
app.secret_key = 'my_super_secret_key'
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(report_blueprint, url_prefix="/report")

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/static')
def static_html():
    return render_template('index.html')

@app.route('/dynamic')
def dynamic_html():
    languages = ['C', 'Python', 'C++']
    return render_template(
        'dynamic.html',
        languages = languages
    )

@app.route('/logout')
def logout_handler():
    session.clear()
    return "Goodbye"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)