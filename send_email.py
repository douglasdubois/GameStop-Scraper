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

def send_email(product, subject="", condition="", url="", error=""):
    message = EmailMessage()
    
    message.add_header('Subject', subject if subject == "Error" else f"{condition}: {product}")
    message.add_header('From', email_from)
    message.add_header('To', email_to)
    message.set_content(f"Error for {product}: {error}" if subject == "Error" else f'Available for purchase: {url}')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, message.as_string())
