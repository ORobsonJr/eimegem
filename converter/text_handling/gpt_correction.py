import openai
from decouple import config

SCRIPT = """
Corrija as palavras erradas, gramática e tudo que você encontrar de errado no texto que te passarei, vale ressaltar que não quero texto adicional, apenas o texto devidamente corrigido; texto para corrigir:

"""

openai.api_key = config('API_KEY')

def openai_correction(text:str):
    """
    Correct text using gpt inteligence
    """
    text_solution = SCRIPT + text
    
    response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=text_solution,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
        )
    return response.choices[0].text.strip()
