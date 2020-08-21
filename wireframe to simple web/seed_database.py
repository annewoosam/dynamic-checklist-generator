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

# Load checklist data from JSON file
with open('data/checklists.json') as f:
    checklist_data = json.loads(f.read())

# Create checklists, template, questions and key help items and store them in list so we can use them.

checklists_in_db = []
for checklist in checklist_data:
    template_name, question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_URL, help_text = (
                                   checklist['question'],
                                   checklist['yes_text'],
                                   checklist['no_text'],
                                   checklist['not_applicable_text'],
                                   checklist['category'],
                                   checklist['primary_driver'],
                                   checklist['resource_url'],
                                   checklist['help_text'])

    db_checklist = crud.create_checklist(template_name,
                                 question,
                                 yes_text,
                                 no_text,
                                 not_applicable_text,
                                 category,
                                 primary_driver,
                                 resource_url,
                                 help_text)
    checklist_in_db.append(db_checklist)

# Create 6 users
# docs on generating random users at https://faker.readthedocs.io/en/master/
# can fake addresses, internet providers, text and localize so names appear to be from certain country
for n in range(6):
    email = fake.email()
    password= 'test'
    user_full_name = fake.name()

    user = crud.create_user(email, password, user_full_name)

