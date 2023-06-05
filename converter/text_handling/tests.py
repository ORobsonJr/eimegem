from django.test import TestCase
from converter.text_handling import gpt_correction 

# Create your tests here.
class GptTest(TestCase):
    def gpt_correct(self):
        response = gpt_correction.openai_correction(text="meu bone a jobé")
        print(response)
