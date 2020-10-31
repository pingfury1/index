from app import db

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    items = db.relationship('Item', backref='group')

    def __repr__(self):
        return '<Group %r>' % self.name


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    url = db.Column(db.Unicode)
    notice = db.Column(db.UnicodeText)
    logo_url = db.Column(db.Unicode)
    manual_name = db.Column(db.Unicode)
    manual_url = db.Column(db.Unicode)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __repr__(self):
        return '<Item %r>' % self.name