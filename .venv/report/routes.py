from flask import Blueprint, render_template

report_blueprint = Blueprint(
    'report_blueprint',
    __name__,
    template_folder='templates'
)

@report_blueprint.route('/')
def report_handler():
    return render_template('report_index.html')