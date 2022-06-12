from email_body import *
from email_images import *
from email_sender import *
from email_settings import EMAIL
import random


def main():
    names = ['Joao', 'Maria', 'Ana', 'Pedro']
    name = random.choice(names)
    content = f'Esse foi apenas um email teste para {name}!'

    try:
        html_body = get_html_body(name=name, content=content)
        html_body = convert_html_body(html_body)
        html_image = get_html_image()
        html_content = build_email(to=EMAIL, subject='Email Test', body=html_body, image=html_image)
        send_email(message=html_content)
    except Exception as e:
        print(f'Error: Could not send email -> {e}')
    else:
        print('Success: Email has been sent!')


if __name__ == '__main__':
    main()
