"""
Create RAM_files folder
"""

import os

FOLDER = os.path.join('converter', 'RAM_files')
has_exitence =  os.path.exists(FOLDER)

if has_exitence is False:
    os.mkdir(FOLDER)

#else:
#   Pass, the folder already
