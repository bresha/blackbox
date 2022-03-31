from flask import render_template, request, Blueprint


bp = Blueprint('web', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404