from flask import jsonify
from . import api
from flask_restful import Resource
from ..models import Group, Item
from .. import db

class Items(Resource):
    
    def get(self, item_id=None):
        if not item_id:
            r = [ i.to_json() for i in Item.query.all() ]
            return jsonify(r)
        else:
            r = Item.query.filter_by(id=item_id).first_or_404().to_json()
            return jsonify(r)


class Groups(Resource):
    def get(self, group_id=None):
        if not group_id:
            r = [ g.to_json() for g in Group.query.all() ]
            print(r)
            return jsonify(r)
        else:
            r = Group.query.filter_by(id=group_id).first_or_404().to_json()
            return jsonify(r)