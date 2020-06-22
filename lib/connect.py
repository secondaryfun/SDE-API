from peewee import *
from dotenv import load_dotenv
import os

project_folder = os.path.expanduser('../')
load_dotenv(os.path.join(project_folder, '.env'))

DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')

db = PostgresqlDatabase('spm', user=DB_USER,
                        password=DB_PASS, host='localhost', port=5432)

db.connect()
