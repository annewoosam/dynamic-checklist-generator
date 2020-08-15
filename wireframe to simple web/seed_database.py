"""Script to seed database."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system('dropdb checklists')
os.system('createdb checklists')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/checklists.json') as f:
    checklist_data = json.loads(f.read())

# Create templates,questions, store them in list so we can use them

checklists_in_db = []
for checklist in checklist_data:
    question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_URL, help_text = (
                                   checklist['question'],
                                   checklist['yes_text'],
                                   checklist['no_text']),
                                   checklist['not_applicable_text'],
                                   checklist['category'],
                                   checklist['primary_driver'],
                                   checklist['resource_url'],
                                   checklist['help_text'])

    db_checklist = crud.create_checklist(question,
                                 yes_text,
                                 no_text,
                                 not_applicable_text,
                                 category,
                                 primary_driver,
                                 resource_url,
                                 help_text)
    checklist_in_db.append(db_checklist)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    user_email = f'user{n}@test.com'  # Voila! A unique email!
    user_password = 'test'

    user = crud.create_user(user_email, user_password)

