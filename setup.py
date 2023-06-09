from os import path

"""
Create and config .env file
"""

DIR_PATH = dir_path = path.dirname(path.realpath(__file__))
ENV_file = path.join(DIR_PATH, '.env')

if path.exists(ENV_file) is False:
    API_KEY = input("\033[36m[ALERT]\033[0m Por favor insira sua chave API do chat-gpt aqui: ")

    try:
        with open(ENV_file, 'w') as f:
            f.write('API_KEY=' + API_KEY)
            print("\033[32m[SUCCESS]\033[0m Arquivo .env criado com sucesso!\nem caso de chave errada ou para reconfigurar por favor exclua o arquivo .env e execute novamente.")
    
    except Exception as e:
        print("\033[31m[ERROR]\033[0m ", e)

else:
    print("\033[31m[ERROR]\033[0m O arquivo .env já existe, exclua ele caso queira reconfigurar.")
