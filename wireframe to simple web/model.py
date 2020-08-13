"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///checklists', echo=True):
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
# test_user = User(user_email='test@test.test', user_password='test')   
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
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_name = db.Column(db.String)
    user_type = db.Column(db.String)
 # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.user_email}>'

# create models class
class Checklist(db.Model):
    """A checklist."""
    # master checklist start
    __tablename__ = 'checklist'

    checklist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creator_id = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    checklist_name = db.Column(db.String)

    # see also checklistItems for questions associated with Checklist
    
    # spin-off checklist elements

    # provided when preparer clones checklist
    who_for = db.Column(db.String) # such as a person, client, employer or client number that could mix numbers and characters
    checklist_time_frame = db.Column(db.String) # such as 01/2020, 2020, Spring 2020, Q1 2020
   
    preparer_name = db.Column(db.String) # must ADD. Will know e-mail and should populate user_name/update. Each checklist has a preparer whose name must
    # appear on reports and must be able to receive notifications.

    # populated by preparer click event
    date_sent_to_review = db.Column(db.DateTime) # preparer/ populated by on-click event

    reviewer_name = db.Column(db.String) # must ADD. May know e-mail and should populate user_name/update. Each checklist has a reviewer whose name must
    # appear on reports and must be able to receive notifications. If does not exist, need to create with a default password.

    # populated by reviewer click events
    date_review_completed = db.Column(db.DateTime) # reviewer/populated by on-cick event
    
    recipient_name= db.Column(db.String) # must ADD. May know e-mail. Does not need to add password. Each checklist has a recipient whose name must
    # appear on reports and must be able to receive notifications. However, the recipient does not need to access the checklist site.

    date_sent_to_recipient = db.Column(db.DateTime) # reviewer/ populated by on-click event

    # in sum, added slots for preparer_name, reviewer_name and recipient_name which will feed back to Users.

    # checklists = a list of checklist objects

    def __repr__(self):
        return f'<Checklist checklist_id={self.checklist_id} checklist_name={self.checklist_name}>'

class ChecklistItems(db.Model):
 
    """A checklist item and its features."""
 
    __tablename__ = 'checklist_item'

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # Text rather than String is for textarea inputs
    question = db.Column(db.Text)
    question_number = db.Column(db.Integer)
    yes_text = db.Column(db.Text)
    no_text = db.Column(db.Text)
    not_applicable_text = db.Column(db.Text)
    # when an answer is skipped the question will be reprinted for the preparer
    primary.driver = db. Column(db.Boolean) # when a preparer enters NA for this any item with the same category will be switched to NA
    # we still want to print these sub-questions so other viewers understand that the items wewre not dropped in error.
    category = db.Column(db.String)

    def __repr__(self):
        return f'<ChecklistItems item_id={self.item_id} question={self.question}>'

class VideoURL(db.Model):

    """A checklist item's associated video, if any. Many will not have"""
 
    __tablename__ = 'video_url'

    video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    checklist_id = db.Column(db.Integer)
    question_number = db.Column(db.Integer)
    video_url=db.column(db.String)


    def __repr__(self):
        return f'<VideoURLs video_id={self.video_id} video_url={self.video_url}>'

class HelpText(db.Model):

    """A checklist item's associated help text, if any. Many will not have"""
 
    __tablename__ = 'help_text'

    help_text_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    checklist_id = db.Column(db.Integer)
    question_number = db.Column(db.Integer)
    help_text=db.column(db.Text)
    
    def __repr__(self):
        return f'<HelpText help_text={self.help_text_id} help_text={self.help_text}>'

class UserAnswer(db.Model):

    """A checklist item's preparer responses. Comments only not required"""
 
    __tablename__ = 'preparer_answer'

    user_answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    question_number = db.Column(db.Integer)
    answer = db.column(db.String) # dropdown restricted to y, n, na, blank
    time_spent = db.column(db.Integer)
    user_type = db.column(db.String)  #preparer or user
    
    def __repr__(self):
        return f'PreparerAnswer user_answer_id={self.user_answer_id} question_number={self.question_number} answer={self.answer} time_spent={self.time_spent} user_type={self.user_type}>'

class Answer(db.Model):
    
    """A checklist item's answer options"""
    __tablename__ = 'answer'

    answer_id = db.column(db.String)
    option_preparer = db.column(db.String) # dropdown restricted to y, n, na, blank for yes, no, not applicable
    option_reviewer = db.column(db.String) # dropdown restricted to c, r, na, blank for corrections required, ready and not applicable

def __repr__(self):
        return f'Answer answer_id={self.answer_id} option_preparer={self.option_preparer} option_reviewer={self.option_reviewer}>'

class Comments(db.Model): 
	    """A checklist item's comments. Not all answers will have comments and comments can be made by either preparer or reviewer"""
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    comment = db.column(db.Text) # think preparer comment field should be here
    user_type =db.column(db.String) #preparer or reviewer only

def __repr__(self):
        return f'Comments comment_id={self.comment_id} comment={self.comment} user_type={self.user_type}>'

class ReviewerAnswer(db.Model):
    reviewer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    preparer_answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    preparer_id = db.Column(db.Integer)
    question_number = db.Column(db.Integer)
    answer = db.column(db.String) # dropdown restricted to y, n, na, blank
    time_spent = db.column(db.Integer)

    def __repr__(self):
        return f'<ReviewerAnswer reviewer_answer_id={self.reviewer_answer_id} video_url={self.video_url}>'


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
