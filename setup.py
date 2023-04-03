import platform
import os
import sys
from var import manage
import subprocess


REQUIREMENTS = 'requirements.txt'
EXECUTABLE_FILE = 'start'
OPERATIONAL_SYSTEM = platform.system()
FILE_EXE = os.path.join('setup', 'ocr-install.exe') 





def install_requirements():
    os.system(f'pip3 install -r {REQUIREMENTS}')

class return_pyseract():
    """
    This is just aplicable in Windows system
    """
    

    def install_through_ocr(self):
        import requests

        BITS = 0
        if (sys.maxsize > 2**64) is True:
            BITS = 64

        else:
            BITS = 32

        #Install OCR
        download_url = manage.return_bits_ocr(BITS)
        r = requests.get(download_url)

        with open(FILE_EXE, 'wb') as f:
            f.write(r.content)

        print('[setup] Abrindo arquivo executavel para instalação')
        print('[setup] Por favor, conclua a instalação e faça a configuração na pasta setup')

        try: 
            subprocess.run([FILE_EXE])

        except Exception as e:
            print(e)

        while True:
            #While not receive a valid responde, still True
            response = input('Por favor preencha o diretório do arquivo tesseract.exe: ')

            if os.path.exists(response) is True:
                name_file = os.path.join(os.path.dirname(__file__),
                                        'var',
                                        'ocr_location.txt')
                
                with open(name_file, 'w') as f:
                    f.write(response)




        



def set_converter():
    stringfy_file = os.path.join('converter', 'stringify.py')

    #We need to pull this back to avoid incorrect indentation in the final code
    linux_code = \
    """
import os
from pytesseract import image_to_string
from PIL import Image


def stringfy_image(file):
    content = image_to_string(Image.open(file))
    os.remove(file)
    return content
    """

    # We need to pull this back to avoid incorrect indentation in the final code
    windows_code = \
"""
import os
import pytesseract
from pytesseract import image_to_string
from PIL import Image


def stringfy_image(file):

    seract_location = open(os.path.join(
        os.path.dirname(__file__),
        'var',
        'ocr_location.txt'  
        )

    pytesseract.pytesseract.tesseract_cmd = r"{}".format(seract_location)
    content = image_to_string(Image.open(file))
    os.remove(file)
    return content
"""
    
    if OPERATIONAL_SYSTEM == 'Windows':
        """
        Our process works in the following way...

        For default pyseract is installed in:

        """

        #...

        with open(stringfy_file, 'w') as f:
            f.write(windows_code)

    elif OPERATIONAL_SYSTEM == "Linux":
        with open(stringfy_file, 'w') as f:
            f.write(linux_code)
        
        
if __name__ == '__main__' and sys.argv[1]=='INSTALL':
    install_requirements()

    if OPERATIONAL_SYSTEM == 'Windows':
        try: os.mkdir('setup')
        except: pass

        return_pyseract().install_through_ocr()
        set_converter()



    elif OPERATIONAL_SYSTEM == 'Linux':
        set_converter()



