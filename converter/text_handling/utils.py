from converter.text_handling.similarity_system import text_handling, Database
from converter.text_handling import gpt_correction

def text_correction(text_to_correct: dict):  
    if text_to_correct.get('data'):
        str_to_list_text = text_handling().__main__(text_to_correct['data'])
        
        return str_to_list_text
    
    return text_to_correct + ' is not valid'



def correct_by_gpt(text: str):
    """
    Correct text through Chat-Gpt
    """
    return str(gpt_correction.openai_correction(text))

