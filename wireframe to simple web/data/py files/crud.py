"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
import datetime


"""CRUD operations."""


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# full name and type will be added later - when creating (creator), preparing (for preparer and reviewer) 
# and sending to recipient or providing view access to reporting only viewers. Viewing is a late stage feaure.
# right now the name is for emails and not personalization so we are not splitting first and last name.

# return user by filter for e-mail

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_password(password):
    """Return a user by email."""

    return User.query.filter(User.password == password).first()

def get_users():
    """Return all movies."""

    return User.query.all()

# return user by id for link

def get_user_by_id(user_id):

    return User.query.get(user_id)

# Functions for creating checklist templates, returning a list of all available checklists and
# returning a specific checklist by id.

def create_checklist(user_email, user_name, user_type="creator", checklist_name):
    """Create and return a new movie."""

    checklist = Checklist(user_email=user_email, #passed by session
                  user_name=user_name,
                  user_type=user_type,
                  checklist_name=checklist_name)

    db.session.add(checklist)
    db.session.commit()

    return checklist
    # add  user_name and user_type to User as creator

def get_checklists():
    """Return all checklists."""

    return Checklists.query.all()
 
def get_checklist_by_id(checklist_id):
    """Return checklist by id."""

    return Checklist.query.get(checklist_id)

# Functions for cloning checklist template for preparer, returning a list of all available
# checklists by preparer and returning a specific checklist by id for the preparer.

# Functions for cloning checklist template for reviewer, returning a list of all available
# checklists by reviewer and returning a specific checklist by id for the reviewer.

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
