from application import db

class Winlose(db.Model):
    matchid = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(40), nullable=False)
    opponent = db.Column(db.String(40), nullable=False)
    result = db.Column(db.String(40), nullable=False) 