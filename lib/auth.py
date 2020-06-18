from flask_peewee.auth import auth

from app import app, db
from models import User

auth = Auth(app, db, user_model=User)
