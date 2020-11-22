from flask import jsonify
from flask_restful import Resource, reqparse
from ..models import Group

parse = reqparse.RequestParser()

#args = parse.parse_args()


class Groups(Resource):

    def get(self, group_id=None):
        if not group_id:
            r = [ g.to_json() for g in Group.query.all() ]
            print(r)
            return jsonify(r)
        else:
            r = Group.query.filter_by(id=group_id).first_or_404().to_json()
            return jsonify(r)
    
    def post(self, group_id=None):
        pass