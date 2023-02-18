from PIL import Image
from pytesseract import image_to_string

def img_to_str(file_image: str):
    
    try:
        #Return image text
        return image_to_string(Image.open(file_image))

    except Exception as e:
        return e #for while
