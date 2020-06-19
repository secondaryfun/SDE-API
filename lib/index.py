# App

from peewee import *
from flask import Flask, render_template, request, jsonify
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI, RestResource
from playhouse.shortcuts import model_to_dict, dict_to_model
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

DATABASE = {
    'name': 'spm',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)


# Models


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

# Admin


admin = Admin(app, name='sde_api', template_mode='bootstrap3')
admin.add_view(ModelView(ExploreCard))


# API
api = RestAPI(app)
api.register(ExploreCard)

@app.route('/db/explorecard/', methods=['GET'])
@app.route('/db/explorecard/<id>', methods=['GET'])
def get_items(id=None):
    if id:
        return jsonify(ExploreCard.get(ExploreCard.id == id))
    else:
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        return jsonify(cards)

@app.route('/db/explorecard/name/', methods=['GET'])
@app.route('/db/explorecard/name/<name>', methods=['GET'])
def get_items(name=None):
    if name:
        return jsonify(ExploreCard.get(ExploreCard.name == name))
    else:
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        return jsonify(cards)

@app.route('/db/explorecard/type/', methods=['GET'])
@app.route('/db/explorecard/type/<type>', methods=['GET'])
def get_items(name=None):
    if name:
        return jsonify(ExploreCard.get(ExploreCard.name == name))
    else:
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(person))
        return jsonify(cards)
# Views


@app.route('/')
def homepage():
    return render_template('homepage.html')


# Main
api.setup()


def create_tables():
    db.database.create_tables([ExploreCard], safe=True)


create_tables()
app.run(port=5000, debug=True)
