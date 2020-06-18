import datetime
from peewee import *

# from flask_peewee.auth import BaseUser

from app import db


class BaseModel(db.Model):
    class Meta:
        database = db

# class User(db.Model, BaseUser):
#     username = CharField()
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField(default=datetime.datetime.now)
#     active = BooleanField(default=True)
#     admin = BooleanField(default=False)

#     def __unicode__(self):
#         return self.username


class ExploreCard(db.Model, BaseModel):
    name = CharField()
    sort = CharField()
    # char_type = CharField()
    # affinity = CharField()
    # move = CharField()
    # ap = CharField()
    # strength = CharField()
    # arm = CharField()
    # will = CharField()
    # dex = CharField()
    # heart = CharField()
    # sk_pn = CharField()
    # bit = CharField()
    # abilities = []
    # actions = []
    # card_back = TextField()
    # flavor = TextField()
    # product = []
    # realm = CharField()
