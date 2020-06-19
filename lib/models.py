import datetime
from peewee import *

# from flask_peewee.auth import BaseUser

from connect import db


class BaseModel(Model):
    class Meta:
        database = db


class ExploreCard(BaseModel):
    name = CharField(null=True)
    sort = CharField(null=False, default=None)
    char_type = CharField(null=False, default=None)
    affinity = CharField(null=False, default=None)
    move = IntegerField(null=False, default=None)
    ap = IntegerField(null=False, default=None)
    strength = CharField(null=False, default=None)
    arm = CharField(null=False, default=None)
    will = CharField(null=False, default=None)
    dex = CharField(null=False, default=None)
    heart = IntegerField(null=False, default=None)
    sk_pn = IntegerField(null=False, default=None)
    bit = CharField(null=False, default=None)
    abilities = TextField(null=False, default=None)
    actions = CharField(null=False, default=None)
    card_back = TextField(null=False, default=None)
    flavor = TextField(null=False, default=None)
    product = CharField(null=False, default=None)
    realm = CharField(null=False, default=None)
    status = CharField(null=False, default=None)

# class User(db.Model, BaseUser):
#     username = CharField()
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField(default=datetime.datetime.now)
#     active = BooleanField(default=True)
#     admin = BooleanField(default=False)

#     def __unicode__(self):
#         return self.username
