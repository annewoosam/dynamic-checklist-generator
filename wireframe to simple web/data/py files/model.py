"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

# create user database with  user_id as autoincrementing primary ID;
# to test quite env and createdb ratings. If allready exists; dropdb ratings then createdb ratings again then resume virtual env
# In venv
# ipython -i model.py
# IN
# db.create_all()   
# test_user = User(email='test@test.test', password='test')   
# db.session.add(test_user) 
# db.session.commit()  
# user = User.query.first()
# user 
# OUT
# <User user_id=1 email=test@test.test>
# to regenerate database quit from ipython using quit() then dropdb, createdb and load python3 -i yourfilename/
# then db.create_all()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

 # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

# create models class
class Movie(db.Model):
    """A movie."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

 # ratings = a list of Rating objects

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    #two lines below added create relationships
    #     These can be tested n\in teh venv using
    #     >>> rating = Rating.query.get(1)  # Get a rating by primary key

    # >>> rating.user  # Wow!!
    # <User user_id=100 email=jane@doe.com>
    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')
    
    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
