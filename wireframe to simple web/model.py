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

class Template(db.Model):
    """A template."""
    
    # Master templates established by creators that can be cloned to be checklists for individual clients, employees or personal use.
    __tablename__ = 'template'

    creator_id = db.Column(db.Integer)
    template_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    template_name = db.Column(db.String)
    updated_at = db.Column(db.DateTime)
    
    # After a creator establishes a template they add the questions and help text so that a preparer can spin off a checklist for whomever they need for whatever time frame.
    def __repr__(self):
        return f'<Template template_id={self.template_id} template_name={self.template_name}>'

class TemplateQuestions(db.Model):
 
    """A template question and its features are added one by one by teh creator until finished. Sample templates are in the templates.json file that can be used to seed a demo database."""
 
    __tablename__ = 'template_questions'
    # Text rather than String is for textarea inputs
    template_question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    template_name varchar = db.Column(db.String)
    question_number = db.Column(db.Integer)
    question = db.Column(db.Text)
    yes_text = db.Column(db.Text)
    no_text = db.Column(db.Text)
    not_applicable_text = db.Column(db.Text)
    # when an answer is skipped the question will be reprinted for the preparer
    help_text = db.Column(db.Text)
    resource_url = db.Column(db.String) # input category will be URL. Name resource allows linking of video or any web-resource.
    category = db.Column(db.String)
    primary_driver = db. Column(db.Boolean) # when a preparer enters NA for this any item with the same category will be switched to NA
    # we still want to print these sub-questions so other viewers understand that the items wewre not dropped in error.

    def __repr__(self):
        return f'<TemplateQuestions template_question_id={self.template_question_id} question={self.question}>'

class Checklist(db.Model):
    
    """Once a template is created it may have many questions."""
    
    __tablename__ = 'checklist'
    checklist_id=db.Column(db.Integer, autoincrement=True, primary_key=True) 
    preparer_id = db.Column(db.Integer) # from login on save via create checklist fromn template click
    preparer_full_name = db.Column(db.String) # from login on save via create checklist fromn template click or if not in system added to user on save
    # Will know e-mail and should populate user_name/update. Each checklist has a preparer whose name must
    # appear on reports and must be able to receive notifications.
    template_name varchar = db.Column(db.String) # chosen by clicking on appropriate template link
    # provided when preparer clones checklist
    checklist_who_for = db.Column(db.String) # such as a person, client, employer or client number that could mix numbers and characters
    
    checklist_time_frame = db.Column(db.String) # such as 01/2020, 2020, Spring 2020, Q1 2020

   # once above provided, question data populated by preparer click event

    question_number = db.Column(db.Integer)
    question = db.Column(db.Text)
    help_text = db.Column(db.Text)
    resource_url = db.Column(db.String) # input category will be URL. Name resource allows linking of video or any web-resource.
    category = db.Column(db.String)
    primary_driver = db. Column(db.Boolean) 
  
  # preparer responsible for
    preparer_answer = db.Column(db.String) #//yes/no/na/skipped default
    preparer_time_spent = db.Column(db.Integer)
    preparer_comment = db.Column(db.Text)
    reviewer_full_name = db.Column(db.String) # must ADD. May know e-mail and should populate user_name/update. Each checklist has a reviewer whose name must
    reviewer_email = db.Column(db.String)
    reviewer_id = db.Column(db.Integer)
    date_sent_to_review = db.Column(db.DateTime) # populated by on-click event
    reviewer_comment varchar = db.Column(db.Text)
    # appear on reports and must be able to receive notifications. If does not exist, need to create with a default password.
    
    # reviewer responsible for
    reviewer_answer = db.Column(db.String) #//yes/no/na/skipped default
    reviewer_time_spent = db.Column(db.Integer)
    # populated by reviewer click events
    date_review_completed = db.Column(db.DateTime) # reviewer/populated by on-cick event
    recipient_full_name= db.Column(db.String) # May know e-mail. Does not need to add password. Each checklist has a recipient whose name must
    # appear on reports and must be able to receive notifications. However, the recipient does not need to access the checklist site.
    recipient_email = db.Column(db.String)
    date_sent_to_recipient = db.Column(db.DateTime) # reviewer/ populated by on-click event

    # in sum, added slots for preparer_name, reviewer_name and recipient_name which will feed back to Users.

    # checklists = a list of checklist objects

    def __repr__(self):
        return f'<Checklist checklist_id={self.checklist_id} checklist_name={self.checklist_name}>'

class CorrectionsRequiredAtAnyPoint(db.Model):

    """A checklist item's preparer responses. Comments only not required"""
 
    __tablename__ = 'preparer_answer'

    corrections_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    checklist_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    reviewer_answer = db.column(db.String) # dropdown restricted to y, n, na, blank
    last_saved_at = db.column(db.DateTime)
    
    def __repr__(self):
        return f'CorrectionsRequiredAtAnyPoint checklist_id={self.checklist_id} question_id={self.question_id}>'

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
