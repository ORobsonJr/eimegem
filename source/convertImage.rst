Scrape text from image
=================

.. warning::
   Make sure to handle errors and exceptions properly when using this API route.

``v1/convertImage`` POST JSON
----------------------

The ``v1/convertImage`` route allows you to send desired file in base64 format, extract text from it and return the text.

Parameters
~~~~~~~~
``data`` The JSON key used to send base64 data from image. 
``Example:`` {'data': 'base64 code here'}

Response
~~~~~~~~
- ``200`` The API will respond with a status code of 200 OK and the text scraped. 
- ``500`` Happen some error in server or in client request

Example Usage
~~~~~~~~~~~~~

Here's an example of how to use the ``convertImage`` API route in Python:

.. code-block:: python

   import requests, base64

   url = "https://localhost:8000/v1/convertImage"
   image_path = "path/to/image.jpg"

   with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_image = encoded_string.decode('utf-8')

        files = {'data': base64_image}
        response = requests.post(url, files)

   if response.status_code == 200:
       converted_image = response.content
       # Process the converted image as needed
   else:
       print("Image conversion failed. Status code:", response.status_code)


Remember to handle errors and exceptions appropriately in your code.

Additional Notes
~~~~~~~~~~~~~~~~
- Be aware of limitations and restrictions on the supported image formats, the current supported files formats are 'JPG, PNG, JPEG and PDF'.




