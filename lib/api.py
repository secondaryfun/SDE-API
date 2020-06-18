from flask_peewee.rest import RestAPI, RestResource
from app import app
from models import *

# from auth import auth

# user_auth = UserAuthentification(auth)

api = RestAPI(app)  # To Add for authorization: default_auth=user_auth

api.register(ExploreCard)
