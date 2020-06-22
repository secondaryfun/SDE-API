
from connect import db
from models import *
from views import *
from peewee import *
from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView


admin = Admin(app, name='sde_api', template_mode='bootstrap3')
admin.add_view(ModelView(ExploreCard))


def create_tables():
    db.create_tables([ExploreCard], safe=True)


create_tables()
app.run(port=5000, debug=True)
