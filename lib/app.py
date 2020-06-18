from flask import Flask
from peewee import *

from flask_peewee.db import Database

DATABASE = {
    'name': 'spm',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

# ('spm', user="postgres",
#                         password='password', host='localhost', port=5432)
