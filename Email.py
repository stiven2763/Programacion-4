# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:26:36 2021
"""

from flask import Flask, session
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ingabrahamesh@gmail.com'
app.config['MAIL_PASSWORD'] = 'v25810705'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

with app.app_context():
    msg = Message('Hello World', sender = 'Junaid Baber<uob.cms.uob@gmail.com>',\
                  recipients = ['junaidbaber.cs@gmail.com','junaids.baber@gmail.com'],\
                  reply_to='junaid@gmail.com')
    msg.body = "This is the email body. And this is a demo"
    mail.send(msg)

all_emails = ['ingabrahamesh@gmail.com']
with app.app_context():
    with mail.connect() as conn:
        for email in all_emails:
            message = 'This is Tutorial, ignore it'
            subject = "hello, Mr./Miss"
            msg = Message(recipients=[email],sender = 'Junaid Baber<uob.cms.uob@gmail.com>',\
                          body=message,subject=subject)
            conn.send(msg)

from threading import Thread

# create function which will be excuted in threads

def send_email_thread(msg):
    with app.app_context():
        mail.send(msg)

with app.app_context():
    all_emails = ['ingabrahamesh@gmail.com']
    for email in all_emails:        
        message = 'This is Tutorial, ignore it'
        subject = "hello, Mr./Miss"
        msg = Message(recipients=[email],sender = 'Junaid Baber<uob.cms.uob@gmail.com>',\
                          body=message,subject=subject)
        thr = Thread(target=send_email_thread, args=[msg])
        thr.start()