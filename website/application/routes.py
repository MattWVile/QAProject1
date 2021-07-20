from flask.templating import render_template
from application import app, db
from application.models import Game
from datetime import date

from flask import redirect, url_for, request
from .forms import GameForm, ReviewForm
from .models import Game, Review


@app.route('/')
def home():
    games = Game.query.all()
    return render_template("home.html", games=games)

@app.route('/create/game', methods=['GET', 'POST'])
def creategame(): 
    form = GameForm()
    if request.method == 'POST':
        new_game = Game(title=form.title.data, genre=form.genre.data,dev=form.dev.data)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('creategame.html', form=form) 

@app.route('/read/game/<int:id>')
def readgame(id):
    game = Game.query.get(id)
    all_reviews = Review.query.all()
    reviews =[]
    for review in all_reviews:
        if review.game_id == id:
            reviews.append(review)            
    return render_template("game.html", reviews=reviews, game=game)

@app.route('/update/game/<int:id>', methods=['GET', 'POST'])
def updategame(id):
    game = Game.query.get(id)
    form = GameForm()

    if request.method == 'POST':
        if len(form.title.data) < 1:
            game.title = form.title.data
        if len(form.genre.data) < 1:
            game.genre = form.genre.data
        if len(form.dev.data) < 1:
            game.dev = form.dev.data
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('creategame.html', form=form) 

@app.route('/delete/game/<int:id>')
def deletegame(id):
    game_to_del = Game.query.get(id)
    db.session.delete(game_to_del)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/create/review/<int:id>', methods=['GET', 'POST'])
def createreview(): 
    game_id = Game.query.get(id)
    form = ReviewForm()
    if request.method == 'POST':
        new_review = Review(name=form.name.data, content=form.content.data,date=date.today(),game_id = game_id )
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('createreview.html', form=form) 

@app.route('/update/review/<int:id>', methods=['GET', 'POST'])
def updatereview(id): 
    review = Review.query.get(id)
    form = ReviewForm()
    if request.method == 'POST':
        if len(form.name.data) < 1:
            review.name = form.name.data
            review.date = date.today()
        if len(form.content.data) < 1:
            review.content = form.content.data
            review.date = date.today()
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('updatereview.html', form=form) 

@app.route('/delete/review/<int:id>')
def deletereview(id):
    review_to_del = Review.query.get(id)
    db.session.delete(review_to_del)
    db.session.commit()
    return redirect(url_for('home'))

# @app.route('/read')
# def read():
#     all_tasks = Tasks.query.all()
#     tasks_string = ''
#     for task in all_tasks:
#         tasks_string += '<br>' + task.name + ' ' +  str(task.done)
#     return tasks_string
    

# @app.route('/complete/<int:id>')
# def complete(id):
#     task = Tasks.query.get(id)
#     task.done = True
#     db.session.add(task)
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/uncomplete/<int:id>')
# def uncomplete(id):
#     task = Tasks.query.get(id)
#     task.done = False
#     db.session.add(task)
#     db.session.commit()
#     return redirect(url_for('home'))



