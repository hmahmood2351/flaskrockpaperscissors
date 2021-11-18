from application import db

class Winlose(db.Model):
    matchid = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(40), nullable=False)
    opponent = db.Column(db.String(40), nullable=False)
    result = db.Column(db.String(40), nullable=False)
    dev_id = db.Column(db.Integer, db.ForeignKey('dev.dev_id'))

class Dev(db.Model):
    dev_id = db.Column(db.Integer, primary_key=True)
    dev_name = db.Column(db.String(30))
    dev_match = db.relationship('Winlose', backref = 'dev')
