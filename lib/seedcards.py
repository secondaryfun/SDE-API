from peewee import *
import json, csv, sys
from psycopg2 import connect, Error
from models import *
from connect import db




tables = [ExploreCard]

db.drop_tables(tables)
db.create_tables(tables)

# ExploreCard.select()
#