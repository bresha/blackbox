from flask import render_template, request, Blueprint
import smtplib


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

    gmail_user = 'blackbox.leads.chatbot@gmail.com'
    gmail_password = 'd5NEfd8fxNAKc2b'

    sent_from = gmail_user
    to = ['hrvoje.bresic@gmail.com']
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