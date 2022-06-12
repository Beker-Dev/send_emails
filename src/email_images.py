from email.mime.image import MIMEImage
import os


def get_html_image():
    image_file = '../imgs/bored_ape1.png'

    if os.path.isfile(image_file):
        with open(image_file, 'rb') as img:
            image = MIMEImage(img.read())

        return image
    