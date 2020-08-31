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
    prepareranswer = Answer(checklist_id=checklist_id,
                  question_id=question_id,
                  preparer_answer=preparer_answer,
                  preparer_comment=preparer_comment,
                  preparer_time=preparer_time)

    db.session.add(prepareranswer)
    db.session.commit()

    return prepareranswer

def update_prepareranswer(checklist_id, question_id, preparer_answer, preparer_time, preparer_comment):
    updateprepareranswer = Answer(checklist_id=checklist_id,
                  question_id=question_id,
                  preparer_answer=preparer_answer,
                  preparer_time=preparer_time,
                  preparer_comment=preparer_comment)

    updateprepareranswer=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.preparer_answer:preparer_answer})

    updateprepareranswertime=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.preparer_time:preparer_time})

    updateprepareranswercomment=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.preparer_comment:preparer_comment})

    db.session.commit()

    return updateprepareranswer, updateprepareranswertime, updateprepareranswercomment

def create_revieweranswer(checklist_id, question_id, reviewer_ready, reviewer_time, reviewer_comment):
    revieweranswer = Answer(checklist_id=checklist_id,
                  question_id=question_id,
                  reviewer_ready=reviewer_ready,
                  reviewer_time=reviewer_time,
                  reviewer_comment=reviewer_comment)

    db.session.add(revieweranswer)
    db.session.commit()

    return revieweranswer

def update_revieweranswer(checklist_id, question_id, reviewer_ready, reviewer_time, reviewer_comment):
    updaterevieweranswer = Answer(checklist_id=checklist_id,
                  question_id=question_id,
                  reviewer_ready=reviewer_ready,
                  reviewer_time=reviewer_time,
                  reviewer_comment=reviewer_comment)

    updaterevieweranswer=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.reviewer_ready:reviewer_ready})

    updaterevieweranswercomment=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.reviewer_comment:reviewer_comment})

    updaterevieweranswertime=db.session.query(Answer.checklist_id).filter(Answer.question_id==question_id).update({Answer.reviewer_time:reviewer_time})

    db.session.commit()

    return updaterevieweranswer, updaterevieweranswercomment,updaterevieweranswertime

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

def mark_complete(checklist_id, date_complete)  :
    complete = Checklist(checklist_id=checklist_id,
                  date_complete=date_complete)
    
    date_complete=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.date_complete:date_complete})
    # print(mark_complete)

    db.session.commit()

    return complete

def choose_recipient(checklist_id, recipient_id):
    recipient = Checklist(checklist_id=checklist_id,
                  recipient_id=recipient_id)
    
    recipient=db.session.query(Checklist.checklist_id).filter(Checklist.checklist_id==checklist_id).update({Checklist.recipient_id:recipient_id})
    db.session.commit()
    # update confirmed in sqlalchemy/psql. not causing error on save via web. causing error when trying to pull into table. Clearing cache and reloading worked when fed through 
    # backend. Trying on second checklist.

    return recipient

def create_recipient(user_full_name, email, password) :
    """Create and return a new user."""

    
    user = User(user_full_name=user_full_name, email=email, password=password)
   
    db.session.add(user)
    db.session.commit()

    return user


# 2.0 Kanban functionality for preparer & reviewer

# Lists

# Item response based on what the creator coded when the question was set-up.

# Scorecard Elements: Counts & Percentages 

# Preparer Counts  

# def preparer_to_do_count():
# """preparer answered not applicable count."""
# to_do_per_preparer_counts=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='n').count()
# test case # db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='n').count()
# Received expected response

# def preparer_not_applicable_count():
# """preparer answered not applicable count."""
# not_applicable_per_preparer_counts=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='na').count()
# test case # db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='na').count()
# Received expected response

# def preparer_done_count():
# """preparer answered yes count."""
# done_per_preparer_counts=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='y').count()
# test case # db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='y').count()
# Received expected response

# def prepaper_blanks_count():
# """preparer skipped count."""
# This is a little more complex- it needs to be backed into by taking the total questions and adding up all answers then dividing the difference by the total questions
# blanks_per_preparer_counts=
# test case # db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='y').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='n').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='na').count())
# Received expected response

# Reviewer Counts   

# def reviewer_to_do_count():
# """reviewer answered corrections required count."""
# test case # to_do_per_reviewer_count=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='c').count()
# Received expected response

# def reviewer_not_applicable_count():
# """reviewer answered not applicable count."""
# test case # not_applicable_per_reviewer_count=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='na').count()
# Received expected response

# def reviewer_done_count():
# """reviewer answered ready count."""
# test case # done_per_preparer_count=db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='r').count()
# Received expected response

# def reviewer_blanks_count():
# """reviewer skipped count."""
# This is a little more complex- it needs to be backed into by taking the total questions and adding up all answers then dividing the difference by the total questions
# blanks_per_reviewer_counts=
# test case # db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='c').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='r').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='na').count())
# Received expected response

# Preparer Percentages

# def preparer_to_do_percentage():
# """preparer answer set to no count divided by total questions in checklist, rounded to the nearest two decimal points.""""
# to_do_per_preparer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='n').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='n').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

# def preparer_not_applicable_percentage():
# """preparer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points.""""
# not_applicable_per_preparer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='na').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='na').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

# def preparer_done_percentage():
# """preparer answered yes count divided by total questions in checklist, rounded to the nearest two decimal points.""""
# done_per_preparer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.preparer_answer=='y').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.preparer_answer=='y').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

# Reviewer Percentages

# def reviewer_to_do_percentage():
#  """reviewer answer set to return count divided by total questions in checklist, rounded to the nearest two decimal points.""""
# done_per_reviewer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.reviewer_ready=='c').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='c').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

# def reviewer_not_applicable_percentage():
#  """reviewer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points."""    
# done_per_reviewer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.reviewer_ready=='na').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='na').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

# def reviewer_done_percentage(): 
#  """reviewer answer set to ready for recipient count divided by total questions in checklist, rounded to the nearest two decimal points."""    
# done_per_reviewer_as_percentage=round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==checklist_id).filter(Answer.reviewer_ready=='r').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)
# test case # round(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='r').count()/db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()*100,2)
# Received expected response

#Revisit 

# def reviewer_blanks_percentage():
#  """reviewer left unanswered divided by total questions in checklist, rounded to the nearest two decimal points."""
# blanks_per_reviewer_as_percentage
# test case # round(db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='c').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='r').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='na').count()))/(db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==template_id).count()*100,2)))
# Received expected response from first half. Check last, round and ().

# def preparer_blanks_percentage():
# """preparer left answer at default, skipped count divided by total questions in checklist, rounded to the nearest two decimal points.""""
# This is a little more complex- it needs to be backed into by taking the total questions and adding up all answers then dividing the difference by the total questions
# blanks_per_preparer_as_percentage=
# test case # db.session.query(TemplateQuestion.question_id).group_by("question_id").filter(TemplateQuestion.template_id==1).count()-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='c').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='r').count())-(db.session.query(Answer.checklist_id).group_by("checklist_id").filter(Answer.checklist_id==1).filter(Answer.reviewer_ready=='na').count())
# Received expected response

# Visit

# def reviewer_save_current_answers():

#  anything marked return for corrections to be saved to separate database with date

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
