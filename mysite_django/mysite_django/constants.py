import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#   DB Constants
DB_USER = os.environ['DB_USER']