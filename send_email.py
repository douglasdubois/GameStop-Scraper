import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()
email_from = os.getenv('EMAIL_FROM')
email_to= os.getenv('EMAIL_TO')
password = os.getenv('PASSWORD')

print(email_from)
print(email_to)
print(password)

def send_email(product, url, subject="", condition="", error=""):
    message = EmailMessage()
    
    message.add_header('Subject', subject if subject == "Error" else f"{condition.upper()} - {product}")
    message.add_header('From', email_from)
    message.add_header('To', email_to)
    message.set_content(f"Product: {product}\nError: {error}\nURL: {url}" if subject == "error" else f'{Product} available for purchase at {url}')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, message.as_string())
