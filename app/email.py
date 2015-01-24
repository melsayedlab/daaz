from flask import render_template
from flask.ext.mail import Message
from . import mail

def send_mail(to, subject, template, **kwargs):
  message = Message('DaaZ - '+subject, sender='no-reply@daaz.com', recipients=[to])
  message.body =render_template(template+'.txt', **kwargs)
  mail.send(message)
