import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print ('APP_NAME is {}'.format(os.environ.get('APP_NAME')))
    connection_string =  "sqlite:///" + os.path.join(BASE_DIR, os.getenv("DB_FILE"))
    print(f"connection_string = {connection_string}")
else:
    raise RuntimeError("Not found application configuration")
    