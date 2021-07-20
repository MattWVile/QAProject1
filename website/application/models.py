from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    genre = db.Column(db.String(40))
    dev = db.Column(db.String(50))

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    content = db.Column(db.String(4000))
    date = db.Column(db.DateTime)