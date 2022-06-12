import smtplib
import email_settings
from email.mime.multipart import MIMEMultipart


def send_email(message: MIMEMultipart):
    with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user=email_settings.EMAIL, password=email_settings.PASSWORD)
        smtp.send_message(message)
