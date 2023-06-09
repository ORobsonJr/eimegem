Enhance text through CHAT-GPT
=================

.. warning::
   Make sure to handle errors and exceptions properly when using this API route.

``v1/correct_text`` POST JSON
----------------------

The ``v1/correct_text`` route allows you to enhance the text through correction made by CHAT-GPT.

Parameters
~~~~~~~~
``data`` The JSON key used to send text in string format. 
``Example:`` {'data': 'base64 code here'}

Response
~~~~~~~~
- ``200`` The API will respond with a status code of 200 OK and the enhanced text. 
- ``500`` Happen some error in server or in client request

Example Usage
~~~~~~~~~~~~~

Here's an example of how to use the ``correct_text`` API route in Python:

.. code-block:: python

   import requests

   url = "https://localhost:8000/v1/correct_text"
   text_to_enhance = "O resultado finalll que saio foi ezze"

   text_json = {'data': text_to_enhance}
   response = requests.post(url, text_json)

   if response.status_code == 200:
       improved_text = response.content
   else:
       print("Text enhancement failed. Status code:", response.status_code)


Remember to handle errors and exceptions appropriately in your code.

Additional Notes
~~~~~~~~~~~~~~~~
- Be aware of limitations and restrictions on the supported image formats, the current supported files formats are 'JPG, PNG, JPEG and PDF'.
- Ensure that you has the GPT API key set in your system if you're running it locally



