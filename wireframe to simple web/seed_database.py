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

# templates_in_db = []
# for template in template_data:
#     template_id, template_name, question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_url, help_text = (
#                                    template['template_id'],
#                                    template['template_name'],
#                                    template['question'],
#                                    template['yes_text'],
#                                    template['no_text'],
#                                    template['not_applicable_text'],
#                                    template['category'],
#                                    template['primary_driver'],
#                                    template['resource_url'],
#                                    template['help_text'])

#     db_template = crud.create_template(
#                                  template_name,
#                                  question,
#                                  yes_text,
#                                  no_text,
#                                  not_applicable_text,
#                                  category,
#                                  primary_driver,
#                                  resource_url,
#                                  help_text)
#     template_in_db.append(db_template)
# Create 6 users
# docs on generating random users at https://faker.readthedocs.io/en/master/
# can fake addresses, internet providers, text and localize so names appear to be from certain country


