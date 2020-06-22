from peewee import *
import json
import csv
import sys
from psycopg2 import connect, Error
from models import *
from connect import db


tables = [ExploreCard]

# db.drop_tables(tables)
# db.create_tables(tables)

with open('./explorecards.json') as json_data:
    card_list = json.load(json_data)


for card in card_list:
    for value in card.values():
        if value == "-":
            value = ""

    ExploreCard(
        name=card["NAME"],
        sort=card["Quick Sort"],
        char_type=card["TYPE"],
        affinity=card["AFFINITY"],
        move=card["MOVE"],
        ap=card["AP"],
        strength=card["STR"],
        arm=card["ARM"],
        will=card["WILL"],
        dex=card["DEX"],
        heart=card["HEART"],
        sk_pn=card["SK/PN"],
        bit=card["BIT"],
        abilities=card["ABILITIES"],
        actions=card["ACTIONS"],
        card_back=card["CARD BACK"],
        flavor=card["FLAVOR"],
        product=card["PRODUCT"],
        realm=card["REALM"],
        status=card["STATUS"]
    ).save()
