from application import db
from application.models import Games, Reviews

db.drop_all()
db.create_all()

testgame = Games(title = 'Borderlands 2', genre = 'Looty mcShooty', dev = '2K, Gearbox')
db.session.add(testgame)
db.session.commit()
