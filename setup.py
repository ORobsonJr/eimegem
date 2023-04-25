import os
from setuptools import setup, find_packages

"""
Install requirements and eimegem as package
"""

REQUIREMENTS = 'requirements.txt'

if __name__ == '__main__':
    os.system(f'pip3 install -r {REQUIREMENTS}')
    setup(
        name='eimegem',
        packages=find_packages(),
        author='Robson J',
        version=open('VERSION', 'r').read()
    )

else:
    raise Exception('Please ensure that __name__ is __main__')