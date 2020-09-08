"""CRUD operations."""

from model import db, User, Template, TemplateQuestion, Checklist, Answer, connect_to_db

import datetime

def create_user(email, password, user_full_name):
    """Create and return a new user."""

    user = User(email=email, password=password, user_full_name=user_full_name)

    db.session.add(user)
    
    db.session.commit()

    return user

# full name and type will be added later - when creating (creator), preparing (for preparer and reviewer) 
# and sending to recipient or providing view access to reporting only viewers. Viewing is a late stage feaure.
# right now the name is for emails and not personalization so we are not splitting first and last name.

# return user by filter for e-mail

def get_user_by_name(user_full_name):
    """Return a user by email."""

    return User.query.filter(User.user_full_name == user_full_name).first()

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

# Functions for creating templates, returning a list of all available templates and returning a specific template by id.

def create_template(template_name, created_by, created_on):
    """Create and return a new template."""

    template = Template(template_name=template_name,
                  created_by=created_by,
                  created_on=created_on)

    db.session.add(template)

    db.session.commit()

    return template
    
def get_templates():
    """Return all templates."""

    return Template.query.all()
 
def get_template_by_id(template_id):
    """Return template by id."""

    return Template.query.get(template_id)

# Functions for creating template questions, returning a list of all available template questions and returning a specific template question by id.

def create_question(template_id, question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_url, help_text):
   
    question_number=db.session.query(db.func.max(TemplateQuestion.question_number)).group_by("template_id").filter(TemplateQuestion.template_id==template_id).first()
    
    if question_number:

      question_number=question_number[0]+1

    else:

      question_number=1 

    template_question = TemplateQuestion(template_id=template_id,
                  question_number=question_number,
                  question=question,
                  yes_text=yes_text,
                  no_text=no_text,
                  not_applicable_text=not_applicable_text,
                  category=category,
                  primary_driver=primary_driver,
                  resource_url=resource_url,
                  help_text=help_text)

    db.session.add(template_question)

    db.session.commit()

    return template_question

def get_questions():
    """Return all questions."""

    return TemplateQuestion.query.all()
 
def get_question_by_id(question_id):
    """Return template by id."""

    return TemplateQuestion.query.get(question_id)

# Functions for creating checklists, returning a list of all available checklists and
# returning a specific checklist by id.

def create_checklist(template_id, who_for, time_frame, preparer_id, reviewer_id)  :


    checklist_id=db.session.query(db.func.max(Checklist.checklist_id)).first()
    
    if checklist_id:

      checklist_id=checklist_id[0]+1

    else:

      checklist_id=1 


    checklist = Checklist(checklist_id=checklist_id,template_id=template_id,
                  who_for=who_for,
                  time_frame=time_frame,
                  preparer_id=preparer_id,
                  reviewer_id=reviewer_id)
    
    db.session.add(checklist)

    db.session.commit()

    return checklist

def create_checklist_seed(template_id, who_for, time_frame, preparer_id, reviewer_id)  :

    checklist = Checklist(template_id=template_id,
                  who_for=who_for,
                  time_frame=time_frame,
                  preparer_id=preparer_id,
                  reviewer_id=reviewer_id)
    
    db.session.add(checklist)

    db.session.commit()

    return checklist

def get_checklists():
    """Return all checklists."""

    return Checklist.query.all()
 
def get_checklist_by_id(checklist_id):
    """Return checklist by id."""

    return Checklist.query.get(checklist_id)

# Functions for creating answers, returning a list of all available answers and
# returning a specific answers by id.

def create_prepareranswer(checklist_id, question_id, preparer_answer, preparer_time, preparer_comment):
    
    answer_id=db.session.query(db.func.max(Answer.answer_id)).group_by("answer_id").filter(Answer.answer_id==answer_id).first()
    
    if answer_id:

        answer_id=answer_id[0]+1

    else:

        answer_id=1 

    prepareranswer = Answer(checklist_id=checklist_id,
                  answer_id=answer_id,
                  question_id=question_id,
                  preparer_answer=preparer_answer,
                  preparer_comment=preparer_comment,
                  preparer_time=preparer_time)

    db.session.add(prepareranswer)

    db.session.commit()

    return prepareranswer

def update_prepareranswer(checklist_id, answer_id, preparer_answer, preparer_time, preparer_comment):

    updateprepareranswer = Answer(checklist_id=checklist_id,
                  answer_id=answer_id,
                  preparer_answer=preparer_answer,
                  preparer_time=preparer_time,
                  preparer_comment=preparer_comment)

    updateprepareranswer=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.preparer_answer:preparer_answer})

    updateprepareranswertime=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.preparer_time:preparer_time})

    updateprepareranswercomment=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.preparer_comment:preparer_comment})

    db.session.commit()

    return updateprepareranswer, updateprepareranswertime, updateprepareranswercomment

def update_revieweranswer(checklist_id, answer_id, reviewer_ready, reviewer_time, reviewer_comment):

    updaterevieweranswer = Answer(checklist_id=checklist_id,
                  answer_id=answer_id,
                  reviewer_ready=reviewer_ready,
                  reviewer_time=reviewer_time,
                  reviewer_comment=reviewer_comment)

    updaterevieweranswer=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.reviewer_ready:reviewer_ready})

    updaterevieweranswercomment=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.reviewer_comment:reviewer_comment})

    updaterevieweranswertime=db.session.query(Answer.answer_id).filter(Answer.answer_id==answer_id).update({Answer.reviewer_time:reviewer_time})

    db.session.commit()

    return updaterevieweranswer, updaterevieweranswercomment,updaterevieweranswertime

def get_preparer_count():

    """Return counts for preparer Kanban"""

    to_do_count=Answer.query.filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='n').count()

    done_count=Answer.query.filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='y').count()

    not_applicable_count=Answer.query.filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='na').count()

    not_answered_count=Answer.query.filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='').count()

    return to_do_count, done_count, not_applicable_count, not_answered_count

def get_answers():

    """Return all checklists."""

    return Answer.query.all()

def get_answer_by_id(answer_id):

    """Return answer by id."""

    return Answer.query.get(answer_id)

def mark_datesenttoreview(checklist_id, date_sent_to_review):

    readyforreview = Checklist(checklist_id=checklist_id,
                   date_sent_to_review=date_sent_to_review)
    
    date_sent_to_review=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.date_sent_to_review:date_sent_to_review})
    # print(date_sent_to_review)

    db.session.commit() 

    return readyforreview

def mark_datereviewcompleted(checklist_id, date_review_completed):

    reviewcomplete = Checklist(checklist_id=checklist_id,
                   date_review_completed=date_review_completed)

    date_review_completed=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.date_review_completed:date_review_completed})
    # print(date_review_completed)
    db.session.commit() 

    return reviewcomplete

def mark_complete(checklist_id, date_complete):

    complete = Checklist(checklist_id=checklist_id,
                  date_complete=date_complete)
    
    date_complete=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.date_complete:date_complete})

    db.session.commit()

    return complete

def choose_recipient(checklist_id, recipient_id):

    recipient = Checklist(checklist_id=checklist_id,
                  recipient_id=recipient_id)
    
    recipient=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.recipient_id:recipient_id})
    db.session.commit()

    return recipient

def create_recipient(user_full_name, email, password):

    """Create and return a new user."""

    
    user = User(user_full_name=user_full_name, email=email, password=password)
   
    db.session.add(user)
    db.session.commit()

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
