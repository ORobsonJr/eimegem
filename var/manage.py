import os
from json import load

def return_bits_ocr(bits: int):
    OCR_DOWNLOAD_JSON = 'OCR_download.json'

    ocr_location = os.path.join(os.path.dirname(__file__), 'var', OCR_DOWNLOAD_JSON)

    with open(ocr_location) as f:
        read = load(f)

        if bits == 32:
            return read['32 bits']
        
        elif bits == 64:
            return read['64 bits']
        
        else:
            raise ValueError("Please select 32bits or 64bits")