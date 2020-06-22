import datetime
from peewee import *

# from flask_peewee.auth import BaseUser

from connect import db


class BaseModel(Model):
    class Meta:
        database = db

class ExploreCard(BaseModel):
    name = CharField(null=False)
    sort = CharField(null=True)
    char_type = CharField(null=True)
    affinity = CharField(null=True)
    move = IntegerField(null=True)
    ap = IntegerField(null=True)
    strength = CharField(null=True)
    arm = CharField(null=True)
    will = CharField(null=True)
    dex = CharField(null=True)
    heart = IntegerField(null=True)
    sk_pn = IntegerField(null=True)
    bit = CharField(null=True)
    abilities = TextField(null=True)
    actions = TextField(null=True)
    card_back = TextField(null=True)
    flavor = TextField(null=True)
    product = CharField(null=True)
    realm = CharField(null=True)
    status = CharField(null=True)
