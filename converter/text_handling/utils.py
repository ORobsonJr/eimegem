from converter.text_handling.similarity_system import text_handling, Database

def text_correction(text_to_correct: dict):  
    if text_to_correct.get('data'):
        str_to_list_text = text_handling().__main__(text_to_correct['data'])
        
        return str_to_list_text
    
    return text_to_correct + ' is not valid'



