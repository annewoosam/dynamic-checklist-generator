"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

import faker
from faker import Faker
fake = Faker()

os.system('dropdb dynamic_checklists_db')
os.system('createdb dynamic_checklists_db')

model.connect_to_db(server.app)
model.db.create_all()


# create users before templates
# Create 6 users
# docs on generating random users at https://faker.readthedocs.io/en/master/
# can fake addresses, internet providers, text and localize so names appear to be from certain country
# note that Faker separately randomizes the emails and names so this can appear a little mismatched.

for n in range(6):
    email = fake.email()  # Voila! A unique email!
    password = 'test'
    user_full_name = fake.name()

    user = crud.create_user(email, password, user_full_name)

# Create template, questions, checklist and answer sample data and key help items and store them in list so we can use them.

# load sample template data
with open('data/templates.json') as f:
    template_data = json.loads(f.read())


templates_in_db = []
for template in template_data:
    template_name, created_by, created_on = (
                                   template['template_name'],
                                   template['created_by'],
                                   template['created_on'])

    db_template = crud.create_template(template_name,
                                 created_by,
                                 created_on)
    
    templates_in_db.append(db_template)


# load sample data for template questions
with open('data/template_questions.json') as f:
    template_question_data = json.loads(f.read())

template_questions_in_db = []
for template_question in template_question_data:
    template_id, question_number, question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_url, help_text = (
                                   template_question['template_id'],
                                   template_question['question_number'],
                                   template_question['question'],
                                   template_question['yes_text'],
                                   template_question['no_text'],
                                   template_question['not_applicable_text'],
                                   template_question['category'],
                                   template_question['primary_driver'],
                                   template_question['resource_url'],
                                   template_question['help_text'])

    db_template_questions = crud.create_question(
                                 template_id,
                                 question,
                                 yes_text,
                                 no_text,
                                 not_applicable_text,
                                 category,
                                 primary_driver,
                                 resource_url,
                                 help_text)
    template_questions_in_db.append(db_template_questions)


# load sample checklist data
with open('data/checklists.json') as f:
    checklist_data = json.loads(f.read())


checklists_in_db = []
for checklist in checklist_data:
    template_id, who_for, time_frame, preparer_id, reviewer_id = (
                                   checklist['template_id'],
                                   checklist['who_for'],
                                   checklist['time_frame'],
                                   checklist['preparer_id'],
                                   checklist['reviewer_id'])

    db_checklist = crud.create_checklist(template_id,
                                 who_for,
                                 time_frame,
                                 preparer_id,
                                 reviewer_id)
    
    checklists_in_db.append(db_checklist)

# load sample answer data
# with open('data/prepareranswers.json') as f:
#     prepareranswer_data = json.loads(f.read())


# prepareranswers_in_db = []
# for prepareranswer in prepareranswer_data:
#     checklist_id, question_id, preparer_answer, preparer_time, preparer_comment (
#                                    answer['checklist_id'],
#                                    answer['question_id'],
#                                    answer['preparer_answer'],
#                                    answer['preparer_time'],
#                                    answer['preparer_comment']
#                                    )

#     db_prepareranswer = crud.create_prepareranswer(checklist_id,
#                                  question_id,
#                                  preparer_answer,
#                                  preparer_time,
#                                  preparer_comment)
    
#     prepareranswers_in_db.append(db_prepareranswer)

# with open('data/revieweranswers.json') as f:
#     revieweranswer_data = json.loads(f.read())

# revieweranswers_in_db = []
# for revieweranswer in revieweranswer_data:
#     checklist_id, question_id, reviewer_ready, reviewer_time, reviewer_comment (
#                                    answer['checklist_id'],
#                                    answer['question_id'],
#                                    answer['reviewer_ready'],
#                                    answer['reviewer_time'],
#                                    answer['reviewer_comment']
#                                    )

#     db_revieweranswer = crud.create_revieweranswer(checklist_id,
#                                  question_id,
#                                  reviewer_ready,
#                                  reviewer_time,
#                                  reviewer_comment)
    
#     revieweranswers_in_db.append(db_revieweranswer)