import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()
email_from = os.getenv('EMAIL_FROM')
email_to = os.getenv('EMAIL_TO')
password = os.getenv('PASSWORD')

def send_email(name, url, subject='', condition='', error=''):
    message = EmailMessage()
    
    message.add_header('Subject', f'({subject}) {name}' if subject == 'Error' else f'({condition}) {name}')
    message.add_header('From', email_from)
    message.add_header('To', email_to)
    message.set_content(f'Product: {name}\nURL: {url}\nError: {error}' if subject == 'Error' else f'Product: {name}\nURL: {url}')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, message.as_string())
