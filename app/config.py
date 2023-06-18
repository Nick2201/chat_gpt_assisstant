import os
from pathlib import Path
from dotenv import load_dotenv
CONFIG = {}
CONFIG['MAIN'] = str(Path.cwd())
CONFIG['DOCUMENTS'] = str(Path.cwd() / 'docs')

CONFIG.update({
    'DB_CONFIG' : str(Path(CONFIG['DOCUMENTS']) / 'db_connect.json'),
    'PROMTS'    : str(Path(CONFIG['DOCUMENTS']) / 'promts.json'),
    'APP'       : str(Path(CONFIG['MAIN']) / 'app'),
    'API_KEYS'  : str(Path(CONFIG['DOCUMENTS']) / 'key.txt')

})
CONFIG.update({
    'MODELS'    : str(Path(CONFIG['APP']) / 'model')

})
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)
if __name__ == '__main__':

    print(
    CONFIG['MAIN'] ,
    CONFIG['DOCUMENTS'],
    CONFIG['DB_CONFIG'],
    CONFIG['PROMTS'],
    CONFIG['APP'],
    CONFIG['API_KEYS'],



    )
