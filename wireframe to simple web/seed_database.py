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

for n in range(6):
    email = fake.email()  # Voila! A unique email!
    password = 'test'
    user_full_name = fake.name()

    user = crud.create_user(email, password, user_full_name)
    # Load checklist data from JSON file

with open('data/templates.json') as f:
    template_data = json.loads(f.read())

# Create checklists, template, questions and key help items and store them in list so we can use them.

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


# change below to template questions
with open('data/template_questions.json') as f:
    template_question_data = json.loads(f.read())

templates_questions_in_db = []
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

    db_templates_questions = crud.create_template_question(
                                 template_id,
                                 question_number,
                                 question,
                                 yes_text,
                                 no_text,
                                 not_applicable_text,
                                 category,
                                 primary_driver,
                                 resource_url,
                                 help_text)
    templates_questions_in_db.append(db_templates_questions)



