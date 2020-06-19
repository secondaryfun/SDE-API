# App

from flask_admin.contrib.peewee import ModelView
from flask_admin import Admin
from peewee import *
from flask import Flask, render_template, request, jsonify
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI, RestResource
from playhouse.shortcuts import model_to_dict, dict_to_model
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

DATABASE = {
== == == =
from flask_security import Security, PeeweeUserDatastore,
    UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['DATABASE'] = {
    'name': 'spm',
    'engine': 'peewee.PostgresqlDatabase',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

db = Database(app)


# Models

class Role(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)


class User(db.Model, UserMixin):
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)


class UserRoles(db.Model):
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)


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


# Auth
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)


@ app.before_first_request
def create_user():
    for Model in (Role, User, UserRoles):
        # Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)


# Admin


admin = Admin(app, name='sde_api', template_mode='bootstrap3')
admin.add_view(ModelView(ExploreCard))
admin.add_view(ModelView(User))


# API
api = RestAPI(app)
api.register(ExploreCard)

<< << << < HEAD
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

@ app.route('/db/explorecard/type/', methods=['GET'])
@ app.route('/db/explorecard/type/<type>', methods=['GET'])
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
== == == =

>>>>>> > adding security
# Views


@ app.route('/')
@ login_required
def homepage():
    return render_template('homepage.html')


# Main
api.setup()


def create_tables():
    db.database.create_tables([ExploreCard], safe=True)


create_tables()
app.run(port=5000, debug=True)
