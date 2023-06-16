
import os
from pytesseract import image_to_string
from PIL import Image


def stringfy_image(file):
    """
    Scrape text from file image
    """
    content = image_to_string(Image.open(file))
    os.remove(file)
    return content
    