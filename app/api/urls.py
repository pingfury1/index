from flask_restful import Api
from .item import Items
from .group import Groups

from . import api as app_api

api = Api(app_api)

api.add_resource(Items, '/items/', '/items/<int:item_id>/')
api.add_resource(Groups, '/groups/', '/groups/<int:group_id>/')