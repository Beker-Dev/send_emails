from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from datetime import datetime
import os
import email_settings


def get_html_body(name: str, content: str) -> str:
    html_file = '../templates/email_template_1.html'
    actual_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if os.path.isfile(html_file):

        with open(html_file, 'r') as file:
            template = Template(file.read())

        html_body = template.substitute(name=name, content=content, date=actual_datetime)

        return html_body


def convert_html_body(html_body: str):
    if isinstance(html_body, str):
        html_body = MIMEText(html_body, 'html')
        return html_body


def build_email(to, subject, body, image=None):
    message = MIMEMultipart()
    message['from'] = email_settings.EMAIL
    message['to'] = to
    message['subject'] = subject
    message.attach(body)

    if image:
        message.attach(image)

    return message
