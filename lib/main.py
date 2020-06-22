
from models import *
from connect import db
from peewee import *
from flask import Flask, jsonify, request
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

app = Flask(__name__)

admin = Admin(app, name='sde_api', template_mode='bootstrap3')
admin.add_view(ModelView(ExploreCard))


@ app.route('/db/explorecard/', methods=['GET'])
@ app.route('/db/explorecard/<id>', methods=['GET'])
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

@ app.route('/db/explorecard/name/', methods=['GET'])
@ app.route('/db/explorecard/name/<name>', methods=['GET'])
def get_names(name=None):
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

@ app.route('/db/explorecard/type/', methods=['GET'])
@ app.route('/db/explorecard/type/<type>', methods=['GET'])
def types(name=None):
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


@ app.route('/')
def homepage():
    return render_template('homepage.html')


def create_tables():
    db.create_tables([ExploreCard], safe=True)


create_tables()
app.run(port=5000, debug=True)

from models import *
from views import *

def create_tables():
    db.database.create_tables([ExploreCard], safe=True)

if __name__ == '__main__':
    create_tables()
    app.run(port=5000, debug=True)
