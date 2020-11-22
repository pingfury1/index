from flask import jsonify, request
from flask_restful import Resource, reqparse
from ..models import Item
from .. import db

parse = reqparse.RequestParser()
parse.add_argument('name', type=str, required=True, help='Item name.')
parse.add_argument('url', type=str, required=True, help='Item url.')
parse.add_argument('notice', type=str, help='Item notice.')
parse.add_argument('logo_url', type=str, help='Item logo image url.')
parse.add_argument('manual_name', type=str, help='Item manual name.')
parse.add_argument('manual_url', type=str, help='Item manual url.')
parse.add_argument('group_id', type=int, help='Item group id.')

#args = parse.parse_args()

class Items(Resource):
    
    def get(self, item_id=None):
        if not item_id:
            r = [ i.to_json() for i in Item.query.all() ]
            return jsonify(r)
        else:
            r = Item.query.filter_by(id=item_id).first_or_404().to_json()
            return jsonify(r)
    
    def post(self):
        args = parse.parse_args()
        print(args['name'])
        r = Item.query.filter_by(name=args['name']).first()
        if not r:
            item = Item(**args)
            db.session.add(item)
            db.session.commit()
            return jsonify({
                'message': 'Creating a successful',
                'status': 200
            })
        else:
            return jsonify({
                'message': '{} existing'.format(args.name),
                'status': 403
            })
