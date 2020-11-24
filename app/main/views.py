from flask import render_template
from . import main
from .. import db
from ..models import Group

@main.route('/')
def index():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)