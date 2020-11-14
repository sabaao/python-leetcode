import os
from dotenv import load_dotenv

print('Before load_env()', os.getenv('DBCONN_STR'))

load_dotenv()

print('After load_env()', os.getenv('DBCONN_STR'))
