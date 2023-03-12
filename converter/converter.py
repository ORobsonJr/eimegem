from PIL import Image
from pytesseract import image_to_string
import os
import base64
import string
from os.path import exists
from random import choice

def img_to_str(file_location: str):
    """
    Scrape text of an image and return it 
    """
    try:
        content = image_to_string(Image.open(file_location))

        #Remove the file to avoid over storage
        os.remove(file_location)
        return content

    except Exception as e:
        try:
            os.remove(file_location)
        except:
            pass
        
        return {"erro": f"""{e}"""}

def create_file(data):
    """
    Receive the base64 image data and convert to image
    """
    RAM_FILES = os.path.join('converter', 'RAM_files')

    def generate_filename():
        while True:
            letters = string.ascii_lowercase
            #Generate a random filename of up to 15 digits
            random_filename = ''.join(choice(letters) for i in range(15)) + '.png'
            file_ = os.path.join(RAM_FILES, random_filename)

            if exists(file_) is True:
                pass
            
            else: 
                return file_

    #Filter data --> data:image/png;base64... --> to just data
    dataIndex = data['data'].find(',') + 1
    data['data'] = data['data'][dataIndex:]
    
    #Encode to bytes
    encoded_data = str.encode(data['data'])
    filename = generate_filename()

    with open(filename, 'wb') as f:
        f.write(base64.b64decode(encoded_data))
        f.close()

    return filename

    