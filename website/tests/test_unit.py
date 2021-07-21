from flask_testing import TestCase
from flask import url_for
from datetime import date

from application import app, db 
from application.models import Review, Game

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            WTF_CSRF_ENABLED = False
        )

        return app

    def setUp(self):
        db.create_all()

        db.session.add(Game(title='test game', genre = 'test g', dev = 'test dev'))
        db.session.add(Game(title='test game 2', genre = 'test g 2', dev = 'test dev 2'))
        db.session.commit()
        db.session.add(Review(name='test name', content = 'test content', date = date.today(), game_id = 1))
        db.session.commit()
    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

        assert 'test game' in response.data.decode()
    
    def test_read(self):
        response = self.client.get(url_for('readgame', id=1))

        assert 'test game' in response.data.decode()

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('creategame'),
            data = {'title': 'Check create game is working', 'genre': 'genre', 'dev': 'dev'},   
            follow_redirects=True   
            )

        assert "Check create game is working" in response.data.decode()
        assert "genre" in response.data.decode()
        assert "dev" in response.data.decode()

    def test_create_review(self):
        response = self.client.post(
            url_for('createreview', id = 1),
            data = {'name': 'Check create review', 'content': 'content', 'date': date.today()},   
            follow_redirects=True   
            )

        assert "Check create review" in response.data.decode()
        assert "content" in response.data.decode()
        assert str(date.today()) in response.data.decode()

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for('updategame', id=1),
            data = {'title': 'Check update is working'},   
            follow_redirects=True   
            )
        assert "Check update is working" in response.data.decode()
        assert "test g" in response.data.decode()
        assert "test dev" in response.data.decode()
    
    def test_update_game_all(self):
        response = self.client.post(
            url_for('updategame', id=1),
            data = {'title': 'Check update is working', 'genre' : 'test game', 'dev' : 'test deve'},   
            follow_redirects=True   
            )
        assert "Check update is working" in response.data.decode()
        assert "test game" in response.data.decode()
        assert "test deve" in response.data.decode()

    def test_update_review(self):
        response = self.client.post(
            url_for('updatereview', id=1),
            data = {'name': 'Check update is working'},   
            follow_redirects=True   
            )
        assert "Check update is working" in response.data.decode()
        assert "test content" in response.data.decode()
        assert str(date.today()) in response.data.decode()

    def test_update_review_all(self):
        response = self.client.post(
            url_for('updatereview', id=1),
            data = {'name': 'Check update is working', 'content': 'check content' },   
            follow_redirects=True   
            )
        assert "Check update is working" in response.data.decode()
        assert "check content" in response.data.decode()
        assert str(date.today()) in response.data.decode()


class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for('deletegame', id=1),   
            follow_redirects=True   
        )
        assert "test game" not in response.data.decode()
    def test_delete_review(self):
        response = self.client.get(
            url_for('deletereview', id=1),   
            follow_redirects=True   
        )
        assert "test name" not in response.data.decode()

class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_create(self):
        response = self.client.get(url_for('creategame'))
        self.assert200(response)

    def test_update(self):
        response = self.client.get(url_for('updategame', id=1))
        self.assert200(response)

    def test_create_r(self):
        response = self.client.get(url_for('createreview', id=1))
        self.assert200(response)

    def test_update_r(self):
        response = self.client.get(url_for('updatereview', id=1))
        self.assert200(response)