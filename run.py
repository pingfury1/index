from app import create_app, db
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app.run(host='0.0.0.0', debug=True)