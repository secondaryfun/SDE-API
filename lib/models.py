import datetime
from peewee import *

# from flask_peewee.auth import BaseUser

from app import db


# class BaseModel(db.Model):
#     class Meta:
#         database = db


# class ExploreCard(BaseModel):
class ExploreCard(db.Model):
    name = CharField()
    sort = CharField()
    char_type = CharField()
    affinity = CharField()
    move = IntegerField()
    ap = IntegerField()
    strength = CharField()
    arm = CharField()
    will = CharField()
    dex = CharField()
    heart = IntegerField()
    sk_pn = IntegerField()
    bit = CharField()
    abilities = []

# class User(db.Model, BaseUser):
#     username = CharField()
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField(default=datetime.datetime.now)
#     active = BooleanField(default=True)
#     admin = BooleanField(default=False)

#     def __unicode__(self):
#         return self.username
