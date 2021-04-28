from flask_mail import Message
from flask import render_template
from . import main

def welcome_email(subject, template, to, **kwargs):
    sender_email = ""
    
    new_email = Message(subject, sender = sender=sender_email, recipients = [to])
    email.body = render_template(template + '.txt', **kwargs)
    email.body = render_template(template + '.html', **kwargs)
    
    mail.send(new_email)
      