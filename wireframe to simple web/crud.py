"""CRUD operations."""

from model import db, User, Checklist, ChecklistItems, connect_to_db 
import datetime

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

# Functions for adding questions including help items to the checklist

def create_question(question, yes_text, no_text, not_applicable_text, category, primary_driver, video_url, help_text):
    """Create and return a question and help features."""

    checklist_item = Checklist_Item(question=question, #passed by session
                  yes_text=yes_text,
                  no_text=no_text,
                  not_applicable_text=not_applicable_text,
                  category=category,
                  primary_driver=primary_driver,
                  video_url=video_url,
                  help_text=help_text)

    db.session.add(checklist_item)
    db.session.commit()

    return checklist_item

def get_checklist_items():
    """Return all checklist items."""

    return Checklist_items.query.all()
 
def get_checklist_item_by_id(item_id):
    """Return checklist_items by id."""

    return Checklist_items.query.get(checklist_id)

# Functions for cloning checklist template for preparer, returning a list of all available
# checklists by preparer and returning a specific checklist by id for the preparer.
# checklist who for, timeframe, cloning of questions from a specific checklist name and id.
def clone_checklist_id_items(checklist_id):
    clone_checklist_id_item=Clone_checklist_id_item(question=question,
        category=catgeory,
        primary_driver=primary_driver,
        video_url=video_url,
        help_text=help_text)

    for clone_checklist_id_item in clone_checklist_id_items:

    db.session.add(clone_checklist_id_item)
    db.session.commit()

    return clone_checklist_item

def get_cloned_checklist_items():
    """Return all checklist items."""

    return Clone_checklist_id_items.query.all()
 
def get_cloned_checklist_item_by_id(item_id):
    """Return checklist_items by id."""

    return Clone_checklist_items_id.query.get(checklist_id)    

# Kanban functionality for preparer

# Lists

# Item response based on what the creator coded when the question was set-up.

def preparer_to_do_list():
    # preparer answer set to no
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="n":
            print (f"To do:\n")
            print(checklist_item.no_text)

def preparer_not_applicable_list():
    # preparer answer set to not applicable
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="na":
            print (f"Not applicable:\n")
            print(checklist_item.not_applicable_text)

def prepaper_blanks_list():
    # preparer left answer at default, skipped.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="":
            print (f"To answer:\n")
            print(checklist_item.question)

def preparer_done_list():
    # preparer answered yes.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="y":
            print (f"Done:\n")
            print(yes_text)

# Scorecard Elements: Counts & Percentages 

# Counts   

def preparer_to_do_count():
    # preparer answer set to no count.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="n":
            print (f"To do (count): \n", (count(checklist_item.no_text))

def preparer_not_applicable_count():
    # preparer answer set to not applicable count.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="na":
            print (f"Not applicable (count): \n", count(checklist_item.not_applicable_text))

def prepaper_blanks_count():
    # preparer left answer at default, skipped count.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="":
            print (f"To answer (count): \n", (count(checklist_item.question))

def preparer_done_count():
    # preparer answered yes count.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="y":
            print (f"Done (count): \n", count((yes_text))

def preparer_to_do_percentage():
    # preparer answer set to no count divided by total questions in checklist, rounded to the nearest two decimal points.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="n":
            print (f"To do (percent): \n", (count(checklist_item.no_text)/count(checklist_item.question))

def preparer_not_applicable_percentage():
    # preparer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="na":
            print (f"Not applicable (count): \n", count(checklist_item.not_applicable_text)/count(checklist_item.question))

def preparer_blanks_percentage():
    # preparer left answer at default, skipped count divided by total questions in checklist, rounded to the nearest two decimal points.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="":
            print (f"To answer (count): \n", (count(checklist_item.question)/count(checklist_item.question))

def preparer_done_percentage():
    # preparer answered yes count divided by total questions in checklist, rounded to the nearest two decimal points.
    for clone_checklist_id_item in clone_checklist_id_items:
        if preparer_answer.lower()=="y":
            print (f"Done (count): \n", count((yes_text)/count(checklist_item.question))

# Functions for cloning checklist template for reviewer, returning a list of all available
# checklists by reviewer and returning a specific checklist by id for the reviewer.

# Functions for reviewer - saving curent status, minutes and comments. Return to preparer. Send to recipient.

def reviewer_save_current_answers():

# anything marked return for corrections to be saved to separate database with date

def return_to_preparer():
    # psuedo-code
    # if button return for corrections clicked
    # populate the prepare email in to field
    # populate the checklist_name, who for and timeframe and returned for corrections in subject field
    # save the date and time e-mail created to the database

def send_to_recipient():  
    # psuedo-code
    # if button send to recipient clicked
    # populate the recipient email in to field
    # populate the checklist_name, who for and timeframe and ready for delivery in subject field
    # save the date and time e-mail created to the database as date_review_completed and date_sent to recipient

# Kanban functionality for reviewer

# Lists

# Item response based on what the creator coded when the question was set-up.

def reviewer_to_do_list():
    # reviewer answer set to return.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="c":
            print (f"Return for corrections:\n")
            print(no_text)

def reviewer_blanks_list():
    # reviewer left unanswered.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="":
            print (f"Revisit - blank response:\n")
            print(question)

def reviewer_not_applicable_list():
    # reviewer answer set to not applicable.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="na":
            print (f"Not applicable:\n")
            print(not_applicable_text)

def reviewer_done_list():
    # reviewer answer set to ready for recipient.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="r":
            print (f"Ready for delivery:\n")
            print(yes_text)

# Scorecard Elements: Counts & Percentages 

# Counts   

def reviewer_to_do_count():
    # reviewer answer set to return count.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="c":
            print (f"Return for corrections (count):\n", (no_text))

def reviewer_not_applicable_count():
    # reviewer answer set to not applicable count.
        for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="na":
            print (f"Not applicable (count):\n", count(not_applicable_text))

def reviewer_blanks_count():
    # reviewer left unanswered divided by total questions in checklist.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="na":
            print (f"Not applicable (count):\n", count(not_applicable_text))

def reviewer_done_count():
    # reviewer answer set to ready for recipient count divided by total questions.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="r":
            print (f"Ready for delivery (count):\n", count((yes_text))
# Percentages

def reviewer_to_do_percentage():
    # reviewer answer set to return count divided by total questions in checklist, rounded to the nearest two decimal points.
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="c":
            print (f"Return for corrections (count):\n", (no_text)/count(checklist_item.question))

def reviewer_not_applicable_percentage():
    # reviewer answer set to not applicable count divided by total questions in checklist, rounded to the nearest two decimal points.    
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="na":
            print (f"Not applicable (count):\n", count(not_applicable_text)/count(checklist_item.question))

def reviewer_blanks_percentage():
    # reviewer left unanswered divided by total questions in checklist, rounded to the nearest two decimal points.    
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="na":
            print (f"Not applicable (count):\n", count(not_applicable_text)/count(checklist_item.question))

def reviewer_done_percentage(): 
    # reviewer answer set to ready for recipient count divided by total questions in checklist, rounded to the nearest two decimal points.    
    for clone_checklist_id_item in clone_checklist_id_items:
        if review_answer.lower()=="r":
            print (f"Ready for delivery (count):\n", count((yes_text)/count(checklist_item.question))

# Queries - separate file once confirm above working and seed data ready. Call it query.py


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
