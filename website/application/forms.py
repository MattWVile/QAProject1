from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class GameForm(FlaskForm):
    title = StringField('Enter the game title')
    genre = StringField('Enter the game genre')
    dev = StringField('Enter the game developers')
    submit = SubmitField('submit')

class ReviewForm(FlaskForm):
    name = StringField('Enter your name')
    content = StringField('Enter your review')
    submit = SubmitField('submit')
