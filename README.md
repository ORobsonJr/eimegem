<h1 align="center">
  <br>
  Eimegem
  <br>
</h1>

<p align="center">
  <strong>A Powerful Python and Django-based Project for Text Extraction from Images</strong>
</p>

  ![Screenshot_2023-06-09_10-33-11](https://github.com/ORobsonJr/eimegem/assets/109431368/1f8155cb-c69a-4b3f-a7f6-e91fb060efa8)

## Features

- Extract text from various files formats such as JPEG, JPG, PNG, and PDF files.
- Utilizes CHAT-GPT image to enhance text result.
- User-friendly web interface for easy interaction and input of images.

## Demo

Check out the following video to see Eimegem in action:

https://github.com/ORobsonJr/eimegem/assets/109431368/44357b62-1fbe-4faf-8cfd-928fb98ecab6


## Installation & use 

Follow these steps to install eimegem:

| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) Linux  | ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) Install through Docker to other systems (Windows, Mac...) |
| ------------- | ------------- |
| ``` git clone https://github.com/ORobsonJr/eimegem ```  | ``` git clone https://github.com/ORobsonJr/eimegem ``` |
|  ``` virtualenv .venv && source .venv/bin/activate```  | ``` Activate virtualenviroment in your respective system... ``` |
|  ``` pip3 install -r requirements.txt ```  | ``` pip3 install decouple ```  |
|  ``` python3 setup.py ```  | ``` python3 setup.py ``` |
|   | ``` docker build -t eimegem . ``` |

To run through Docker
```
docker run -p 8000:8000 eimegem
```

To run through Linux
```
python3 manage.py runserver
```


## Project documentation 
To checkout project documentation [click here](DEVELOPER.md)
