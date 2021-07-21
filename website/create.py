from application import db
from application.models import Game, Review
from datetime import datetime

db.drop_all()
db.create_all()

testgame = Game(title = 'Borderlands 2', genre = 'Looty McShooty', dev = '2K, Gearbox')
db.session.add(testgame)
db.session.commit()
testreview = Review(name = 'Matt', content = 'IGN 10/10 would play again', date = datetime.today(), game_id = testgame.id)
db.session.add(testreview)
db.session.commit()
