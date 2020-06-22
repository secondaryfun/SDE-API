from peewee import *
from dotenv import load_dotenv
import os
from flask import Flask

project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))

DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
FLASK

db = PostgresqlDatabase('d547nnloq163dj', user=DB_USER,
                        password=DB_PASS, host=DB_HOST, port=5432)

# db = PostgresqlDatabase('spm', user='postgres',
#                         password='password', host='localhost', port=5432)
db.connect()

app = Flask(__name__)
