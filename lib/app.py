from flask import Flask
from peewee import *

from flask_peewee.db import Database

DATABASE = {
    'name': 'spm',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'password': 'password',
}

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)
