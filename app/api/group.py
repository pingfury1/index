from flask import jsonify
from flask_restful import Resource, reqparse
from ..models import Group
from .. import db

parse = reqparse.RequestParser()
parse.add_argument('name')

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
    
    def post(self):
        args = parse.parse_args()
        if not Group.query.filter_by(name=args.name).first():
            group = Group(**args)
            db.session.add(group)
            db.session.commit()
            return jsonify({
                'message': 'Createing a successful',
                'status': 200
            })
        else:
            return jsonify({
                'message': '{} existing'.format(args.name),
                'status': 403
            })