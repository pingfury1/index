from . import api

@api.route('/api', methods=['GET'])
def index():
    return '{"name": "Hello world"}'