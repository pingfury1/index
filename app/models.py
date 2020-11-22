from app import db

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    items = db.relationship('Item', backref='group')

    def __repr__(self):
        return '<Group %r>' % self.name
    
    def to_json(self):
        group_json = {
            'id'    : self.id,
            'name'  : self.name,
            'items' : [
                i.to_json() for i in Item.query.filter_by(group_id=self.id).all()
                ]
        }
        
        return group_json


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
    
    def to_json(self):
        item_json = {
            'id'            : self.id,
            'name'          : self.name,
            'url'           : self.url,
            'notice'        : self.notice,
            'logo_url'      : self.logo_url,
            'manual_name'   : self.manual_name,
            'manual_url'    : self.manual_url,
            'group_id'      : self.group_id
        }

        return item_json