from flask import render_template, request, Blueprint


bp = Blueprint('web', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/send-inquiry', methods=['POST'])
def send_inquiry():
    pass

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404