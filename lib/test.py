from peewee import *
from connect import db
from models import *
from flask import jsonify, Flask
from playhouse.shortcuts import model_to_dict, dict_to_model


app = Flask(__name__)

# from flask import Flask, jsonify, request
# from flask_admin import Admin
# from flask_admin.contrib.peewee import ModelView
# from playhouse.shortcuts import model_to_dict, dict_to_model


card = 'Black Snow'
db_card = ExploreCard.get(ExploreCard.name == card)
print(model_to_dict(db_card))
