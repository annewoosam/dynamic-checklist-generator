"""Based on Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# create user database with  user_id as autoincrementing primary ID;
# to test. If already exists; drop db then create db again then resume virtual env.

# Example flow
# In venv
# ipython -i model.py
# 
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
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_full_name = db.Column(db.String)
    # user_type = db.Column(db.String) - the user type should not be specified if you want people to be able to have multiple roles
    
    templates = db.relationship('Template')
    preparerchecklist = db.relationship('Checklist', foreign_keys="Checklist.preparer_id")
    reviewerchecklist = db.relationship('Checklist', foreign_keys="Checklist.reviewer_id")
    
    # the docs for the relationships are SQLAlchemy multiple join paths
    # the use of templates plural is intentional as there are many templates that can be connected to a user
    # Template is the class
    # The backref is only needed when you want to say the relationship goes both ways without having to state
    # on both tables.
    # However, saving a line causes a lot of scrolling to identify relationships so backrefs are discouraged.

    def __repr__(self):
        return f'<User user_id={self.user_id} user_full_name={self.user_full_name}>'


class Template(db.Model):
    """A template."""
    
    # Master templates established by creators that can be cloned to be checklists for individual clients, employees or personal use.
    __tablename__ = 'templates'

    template_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    template_name = db.Column(db.String)
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_on = db.Column(db.Date)

    # Establish relationships between top and below tables and continue to add as go
    creator=db.relationship('User')
    template_questions=db.relationship('TemplateQuestion')
    # After a creator establishes a template they add the questions and help text so that a preparer can spin off a checklist for whomever they need for whatever time frame.
    # For the template questions we use template_questions with an s for the many questions that belong to one template.
    # Class names should really not be plural because it creates confusion.
    # alt user = db.relationship('User', backref='templates')

    def __repr__(self):
        return f'<Template template_id={self.template_id} template_name={self.template_name}>'

class TemplateQuestion(db.Model):
 
    """A template question and its features are added one by one by teh creator until finished. Sample templates are in the templates.json file that can be used to seed a demo database."""
 
    __tablename__ = 'template_questions'
    # Text rather than String is for textarea inputs
    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    template_id = db.Column(db.Integer,  db.ForeignKey('templates.template_id'))
    question_number = db.Column(db.Integer)
    question = db.Column(db.Text)
    yes_text = db.Column(db.Text)
    no_text = db.Column(db.Text)
    not_applicable_text = db.Column(db.Text)
    # when an answer is skipped the question will be reprinted for the preparer in Sprint 2
    help_text = db.Column(db.Text)
    resource_url = db.Column(db.String) # input category will be URL. Name resource allows linking of video or any web-resource.
    category = db.Column(db.String)
    primary_driver = db. Column(db.Boolean) # when a preparer enters NA for this any item with the same category will be switched to NA
    # we still want to print these sub-questions so other viewers understand that the items wewre not dropped in error.

    # relationship notes

    # we must use template singular and Template singular because 1 templatequestion should have a single relationship to one template.
    
    # by contrast a template question may appear on more than one checklist so we use checklists plural
    
    template = db.relationship('Template')
    
    answers = db.relationship('Answer') # question will have many answers but we will filter to a specific checklist when displaying
    
    def __repr__(self):
        return f'<TemplateQuestions question_id={self.question_id} template_questions={self.question}>'

class Checklist(db.Model):
    
    """Once a template is created it may have many questions."""
    
    __tablename__ = 'checklists'
    
    checklist_id=db.Column(db.Integer, autoincrement=True, primary_key=True) 
    template_id = db.Column(db.Integer, db.ForeignKey('templates.template_id')) # chosen by clicking on appropriate template link
    who_for = db.Column(db.String) # such as a person, client, employer or client number that could mix numbers and characters
    time_frame = db.Column(db.String) # such as 01/2020, 2020, Spring 2020, Q1 2020
    preparer_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) # from login on save via create checklist fromn template click
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date_sent_to_review = db.Column(db.DateTime) # populated by on-click event
    date_review_completed = db.Column(db.DateTime) # reviewer/populated by on-cick event
    
    # Relationships
    
    # Note the special way that the foreign keys for user_id are handled here and in Users

    template = db.relationship('Template')
    preparer = db.relationship('User', foreign_keys=[preparer_id])
    reviewer = db.relationship('User', foreign_keys=[reviewer_id])
    answers = db.relationship('Answer')

    #(link through relationship to answers: answer, time-spent, comments by either preparer or reviewer role)

    def __repr__(self):
        return f'<Checklist checklist_id={self.checklist_id} template_id={self.template_id} who_for={self.who_for} time_frame={self.time_frame}>'

class Answer(db.Model):
    """Data model for an answer."""

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklists.checklist_id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('template_questions.question_id'), nullable=False)
    preparer_answer = db.Column(db.String(), nullable=True) # answers restricted to y, n, n/a, blank. Yes is Done, No is To Do, N/A is not applicable. 
    preparer_time = db.Column(db.Integer, nullable=True)
    preparer_comment = db.Column(db.String(), nullable=True) # answers restricted to c,r, n/a, blank. C is Corrections Required and R is Ready for Delivery.
    reviewer_ready = db.Column(db.Boolean, nullable=True)
    reviewer_time = db.Column(db.Integer, nullable=True)
    reviewer_comment = db.Column(db.String(), nullable=True)
    complete = db.Column(db.Boolean, nullable=True)

    # Relationships
    checklist = db.relationship('Checklist')
    template_question = db.relationship('TemplateQuestion')

    def __repr__(self):
        """Provide helpful representation when printing."""

        return f'<answer answer_id={self.answer_id}'
 
# make sure your database name is correct below

def connect_to_db(flask_app, db_uri='postgresql:///dynamic_checklists_db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

# when done move on to crud.py and seed.py with faker and json if applicable or create sql database code with stdin tab separated table data or with csv and single quotes versions
# other ways we have been shown to use data are input fields, reading strings, importing and parsing text files separated by commas and pipes or rows or a combination.

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
