import smtplib
from flask import flash, redirect, url_for, render_template
from itsdangerous import URLSafeTimedSerializer
from flask.views import MethodView
#from chat import app
from app import app
from flask_login import current_user
from mailer import Message

# generate a token
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECRET_KEY'])

# confirm the token for 3600 seconds.
def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECRET_KEY'],
            max_age=expiration
        )
    except:
        return False
    return email

#email sending with an old easy and poor service
def send_email(user, pwd, recipient, subject, body):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = Message(From=user,
                      To=recipient)
    message.Subject = subject
    message.Html = body

    # Prepare actual message
    #message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    #""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    #print(message)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        print("tls started")
        server.login(gmail_user, gmail_pwd)
        print("log in succesfull")
        server.sendmail(FROM, TO, message.as_string())
        print('successfully sent the mail')
        server.close()
        print("server closed")
    except smtplib.SMTPException as error:
        print (str(error))
        print ("fail")

