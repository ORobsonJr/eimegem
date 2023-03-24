from PIL import Image
from pytesseract import image_to_string
import os
import base64
import string
from os.path import exists
from random import choice
from pdf2image import convert_from_path
 

class ConvertObject():

    def __init__(self):
        self.RAM_FILES = os.path.join('converter', 'RAM_files')

        
    def img_to_str(self, files):
        """
        Scrape text of an image and return it 
        """

        try:
            if type(files) is list:
                #Probably we're working with pdf files
                metadatas = []

                for f in files:
                    content = image_to_string(Image.open(f))
                    os.remove(f)
                    metadatas.append(content)
                return metadatas


            if type(files) is str:
                #Probably a single file
                content = image_to_string(Image.open(files))
                os.remove(f)
                return content
            
            else:
                raise TypeError("The files keyword type is not suported")

        except Exception as e:
            return {"erro": f"""{e}"""}
        

    def generate_filename(self):
        """
        Generate a random filename and concatenate with a directory
        """

        while True:
            letters = string.ascii_lowercase

            #Generate a random filename of up to 15 digits
            random_filename = (
                ''.join(choice(letters)
                for i in range(15))
            )
            
            file_ = os.path.join(self.RAM_FILES, random_filename)

            if exists(file_) is True:
                pass
            
            else: 
                return file_


    def create_file(self, request):
        """
        Receive a JSON response and create a file based on this

        Currently 23/03/2023 the JSON object looks like this:
        {"data": base64 content, "dataType": file extension - pdf, jpeg, png...}
        """
        

        #File extension
        data_type = request['dataType']

        #Let's filter base64 to just content and remove unecessary metadata
        dataIndex = request['data'].find(',') + 1
        request['data'] = request['data'][dataIndex:]
        
        #Encode to bytes
        encoded_data = str.encode(request['data'])
        filename = (
            ConvertObject().generate_filename()
            + '.{}'.format(data_type)
        )

        #Create file
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(encoded_data))
            f.close()

        if data_type =='pdf':
            images = convert_from_path(filename)
 
            files = []
            BASE_FILENAME = ConvertObject().generate_filename()

            for i in range(len(images)):
                # Save pages as images in the pdf
                name_file = BASE_FILENAME+str(i)+'.jpg' 
                images[i].save(name_file, 'JPEG')
                files.append(name_file)

            
            os.remove(filename)
            return files
        
    
        else:
            return filename
    

    
    