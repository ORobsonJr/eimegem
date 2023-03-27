import platform
import os, fnmatch
import sys
from var import manage
import requests
import subprocess


REQUIREMENTS = 'requirements.txt'
EXECUTABLE_FILE = 'start'
OPERATIONAL_SYSTEM = platform.system()
PYSERACT_CMD_LOCATION = ''




def install_requirements():
    os.system(f'pip3 install -r {REQUIREMENTS}')

class return_pyseract():
    """
    This is just aplicable in Windows system
    """
    
    def browse_disk(self):
        """
        Browse disk even find a good candidate to our request
        """

        pattern = 'tesseract.exe'
        path = 'C:'

        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        if result:
            return result[0]
        
    
    def install_through_ocr(self):
        BITS = 0
        if (sys.maxsize > 2**64) is True:
            BITS = 64

        else:
            BITS = 32

        #Install OCR
        download_url = manage.return_bits_ocr(BITS)
        r = requests.get(download_url)

        file_exe = os.path.join('ocr-install.exe') 
        with open(file_exe, 'wb') as f:
            f.write(r.content)

        print('[setup] Abrindo arquivo executavel para instalação')
        print('[setup] Por favor, conclua a instalação e faça a configuração na pasta setup')

        subprocess.run([file_exe])



def set_converter():
    stringfy_file = os.path.join('converter','stringify.py')

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
f"""
import os
import pytesseract
from pytesseract import image_to_string
from PIL import Image


def stringfy_image(file):
    pytesseract.pytesseract.tesseract_cmd = r"{PYSERACT_CMD_LOCATION}"
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
        os.mkdir('setup')
        result = return_pyseract().browse_disk()

        if result:
            PYSERACT_CMD_LOCATION = result
            set_converter()

        else:
            return_pyseract().install_through_ocr()

    elif OPERATIONAL_SYSTEM == 'Linux':
        set_converter()



