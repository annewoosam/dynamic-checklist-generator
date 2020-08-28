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

# Functions for creating templates, returning a list of all available templates and
# returning a specific template by id.

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

# Functions for creating template questions, returning a list of all available template questions and
# returning a specific template question by id.

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

def create_revieweranswer(checklist_id, question_id, reviewer_ready, reviewer_time, reviewer_comment):
    revieweranswer = Answer(checklist_id=checklist_id,
                  question_id=question_id,
                  reviewer_ready=reviewer_ready,
                  reviewer_time=reviewer_time,
                  reviewer_comment=reviewer_comment)

    db.session.add(revieweranswer)
    db.session.commit()

    return revieweranswer

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
    # print(date_review_completed)

    db.session.commit()

    return complete

# def choose_recipient(checklist_id, recipient_id):
#     recipient = Checklist(checklist_id=checklist_id,
#                   recipient_id=recipient_id)
    
#     db.session.add(recipient)
#     db.session.commit()

#     return recipient

def create_recipient(checklist_id, user_full_name, email, password) :
    """Create and return a new user."""

    user = User(user_full_name=user_full_name, email=email, password=password)
    checklist_id=checklist_id
    db.session.add(user)
    db.session.commit()

    return user


# 2.0 Kanban functionality for preparer

# Lists

# Item response based on what the creator coded when the question was set-up.
# mail to integrated for send to reviewer

# Integrated

# # Scorecard Elements: Counts & Percentages 

# # Counts   

# def preparer_to_do_count():
#     # preparer answer set to no count.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="n":
#             print (f"To do (count): \n", (count(checklist_item.no_text))

# def preparer_not_applicable_count():
#     # preparer answer set to not applicable count.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="na":
#             print (f"Not applicable (count): \n", count(checklist_item.not_applicable_text))

# def prepaper_blanks_count():
#     # preparer left answer at default, skipped count.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="":
#             print (f"To answer (count): \n", (count(checklist_item.question))

# def preparer_done_count():
#     # preparer answered yes count.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="y":
#             print (f"Done (count): \n", count((yes_text))

# # Percentages

# def preparer_to_do_percentage():
#     # preparer answer set to no count divided by total questions in checklist, rounded to the nearest two decimal points.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="n":
#             print (f"To do (percent): \n", (count(checklist_item.no_text)/count(checklist_item.question))

# def preparer_not_applicable_percentage():
#     # preparer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="na":
#             print (f"Not applicable (count): \n", count(checklist_item.not_applicable_text)/count(checklist_item.question))

# def preparer_blanks_percentage():
#     # preparer left answer at default, skipped count divided by total questions in checklist, rounded to the nearest two decimal points.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="":
#             print (f"To answer (count): \n", (count(checklist_item.question)/count(checklist_item.question))

# def preparer_done_percentage():
#     # preparer answered yes count divided by total questions in checklist, rounded to the nearest two decimal points.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if preparer_answer.lower()=="y":
#             print (f"Done (count): \n", count((yes_text)/count(checklist_item.question))

# # Functions for cloning checklist template for reviewer, returning a list of all available
# # checklists by reviewer and returning a specific checklist by id for the reviewer.

# # Functions for reviewer - saving curent status, minutes and comments. Return to preparer. Send to recipient.

# def reviewer_save_current_answers():

#  anything marked return for corrections to be saved to separate database with date



# # Kanban functionality for reviewer

# # Lists
# Integrated return for corrections and notify recipient.
# # Item response based on what the creator coded when the question was set-up.

# def reviewer_to_do_list():
#     # reviewer answer set to return.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="c":
#             print (f"Return for corrections:\n")
#             print(no_text)

# def reviewer_blanks_list():
#     # reviewer left unanswered.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="":
#             print (f"Revisit - blank response:\n")
#             print(question)

# def reviewer_not_applicable_list():
#     # reviewer answer set to not applicable.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="na":
#             print (f"Not applicable:\n")
#             print(not_applicable_text)

# def reviewer_done_list():
#     # reviewer answer set to ready for recipient.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="r":
#             print (f"Ready for delivery:\n")
#             print(yes_text)

# # Scorecard Elements: Counts & Percentages 

# # Counts   

# def reviewer_to_do_count():
#     # reviewer answer set to return count.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="c":
#             print (f"Return for corrections (count):\n", (no_text))

# def reviewer_not_applicable_count():
#     # reviewer answer set to not applicable count.
#         for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="na":
#             print (f"Not applicable (count):\n", count(not_applicable_text))

# def reviewer_blanks_count():
#     # reviewer left unanswered divided by total questions in checklist.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="na":
#             print (f"Not applicable (count):\n", count(not_applicable_text))

# def reviewer_done_count():
#     # reviewer answer set to ready for recipient count divided by total questions.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="r":
#             print (f"Ready for delivery (count):\n", count((yes_text))
# # Percentages

# def reviewer_to_do_percentage():
#     # reviewer answer set to return count divided by total questions in checklist, rounded to the nearest two decimal points.
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="c":
#             print (f"Return for corrections (count):\n", (no_text)/count(checklist_item.question))

# def reviewer_not_applicable_percentage():
#     # reviewer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points.    
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="na":
#             print (f"Not applicable (count):\n", count(not_applicable_text)/count(checklist_item.question))

# def reviewer_blanks_percentage():
#     # reviewer left unanswered divided by total questions in checklist, rounded to the nearest two decimal points.    
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="na":
#             print (f"Not applicable (count):\n", count(not_applicable_text)/count(checklist_item.question))

# def reviewer_done_percentage(): 
#     # reviewer answer set to ready for recipient count divided by total questions in checklist, rounded to the nearest two decimal points.    
#     for clone_checklist_id_item in clone_checklist_id_items:
#         if review_answer.lower()=="r":
#             print (f"Ready for delivery (count):\n", count((yes_text)/count(checklist_item.question))

# # Queries - separate file once confirm above working and seed data ready. Call it query.py


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
