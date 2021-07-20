from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    dev = db.Column(db.String(50), nullable=False)
    reviews = db.relationship('Review', backref='game')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(4000), nullable=False)
    date = db.Column(db.DateTime)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)