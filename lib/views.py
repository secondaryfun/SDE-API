from flask import render_template, jsonify
from connect import app, db
from models import *
from playhouse.shortcuts import model_to_dict, dict_to_model


@app.route('/db/explorecard/', methods=['GET', 'POST'])
def get_card_data():
    if request.method == 'GET':
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(card))
        return jsonify(cards)
    elif request.method == 'POST':
        new_card = dict_to_model(ExploreCard, request.get_json())
        new_card.save()
        return jsonify(new_card.name + ' Card Created')


@app.route('/db/explorecard/<card>', methods=['GET', 'PUT', 'DELETE'])
def get_card_data_id(card=None):
    db_card = ExploreCard.get(ExploreCard.id == card)
    if request.method == 'GET':
        return jsonify(model_to_dict(db_card))
    elif request.method == 'PUT':
        items = list(request.get_json().items())
        for item in items:
            card_update = ExploreCard.update(
                {item[0]: item[1]}).where(ExploreCard.id == db_card)
            card_update.execute()
        return jsonify(item)
    elif request.method == 'DELETE':
        deleted_name = model_to_dict(db_card)['name']
        db_card.delete_instance()
        return 'DELETED: ' + deleted_name


@ app.route('/db/explorecard/name/', methods=['GET'])
@ app.route('/db/explorecard/name/<name>', methods=['GET'])
def get_names(name=None):
    if name:
        return jsonify(model_to_dict(ExploreCard.get(ExploreCard.name == name)))
    else:
        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(card))

        cards = []
        for card in ExploreCard.select():
            cards.append(model_to_dict(card))
        return jsonify(cards)


@ app.route('/db/explorecard/type/<type>', methods=['GET'])
def types(type):
    cards = []
    for card in ExploreCard.select().where(ExploreCard.sort == type):
        cards.append(model_to_dict(card))

    return jsonify(cards)
