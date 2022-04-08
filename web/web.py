from flask import render_template, request, Blueprint
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


bp = Blueprint('web', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/inquiry', methods=['POST'])
def send_inquiry():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    inquiry = request.form['inquiry']

    body = f"Please contact {name} via {email} or {phone}!"
    body += "\n Inquiry"
    body += f"\n {inquiry}"

    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_PASSWORD')

    sent_from = gmail_user
    to = [os.getenv('SEND_MAIL_TO')]
    subject = "Webpage lead"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


    return render_template('form_submitted.html')

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404