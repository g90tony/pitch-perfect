from flask_mail import Message
from flask import render_template
from . import mail

def welcome_email(subject, template, to, **kwargs):
    sender_email = "ctstudios254@gmail.com"
    
    email = Message(subject, sender=sender_email, recipients = [to])
    email.body = render_template(template + '.txt', **kwargs)
    email.body = render_template(template + '.html', **kwargs)
    
    mail.send(email)
      