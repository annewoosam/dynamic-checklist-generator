"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.

Be sure to read the instructions before you get started.
"""
from flask_sqlalchemy import SQLAlchemy

from model import db, Human, Animal


##############################################################################
# PART 2: QUERIES
# note the database must be created and populated before the virtualenv is entered then model.py is launched from there

def q1():
    """Return the human with the id 2."""

    # confirmed against database.sql visual check and terminal db query
    # couldn't see in lecture
    # lecture sent to SQLAlchemy Docs
    # SQLAlchemy docs sent to https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/
    # Two column query not available so best guess based on single column query

    # SQL version
    
    # return SELECT fname, lname FROM humans WHERE human_id=2;
    
    #Estimated SQLAlchemy version.Note no  ;

           #Chaining SQL Alchemy2  
           # all_emps = db.session.query(Employee.employee_id, Employee.name)
           # just_ca = all_emps.filter(Employee.state == 'CA')
           # >>> just_ca.all()
    # all_humans = db.session.query(Humans.fname, Humans.lname)
    # just_id2 = all_humans.filter(Humans.human_id == 2)

    # return  just_id.all()
    # *note had to add .all() etc to get to work in env running interactively so did more than just reference object at memory*
    # then called as q1() etc at prompt and checked results visually against database.sql
    # might want to reconfirm .all() etc in both lectures ad no just 1st ones slides as 1st deals only with one db instance
    # Jane Doe
    return Human.query.filter(Human.human_id == 2).all()

def q2():
    """Return the FIRST animal with the species 'fish'."""

    # SQL version. Confirmed.
    # return SELECT name FROM animals WHERE animal_species='fish' LIMIT 1;

    # Estimated SQLALchemy version. Note no ;
    # all_animals = db.session.query(Animals.name)
    # just_fish = all_animals.filter(Animals.animal_species == 'fish').one()
    # return just_fish.all()
    # docs sample is s.query(Department).filter(Department.name == 'IT').one()
    # Bubbles
    return Animal.query.filter(Animal.animal_species == 'fish').one()   

def q3():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """
    # confirmed against database.sql visual check and terminal db query. Watch out for quotes that become backticks.

    # return SELECT name FROM animals WHERE birth_year>2015 AND birth_year IS NOT NULL;

    # Employee.query.filter(Employee.state.isnot(None))   # IS NOT NULL
    # Employee.query.filter(Employee.salary > 70000)
    # q = Employee.query
    # q.filter(Employee.state == 'CA', Employee.salary > 70000)
    # OR q.filter( (Employee.state == 'CA') & (Employee.salary > 70000) )
    # Squiggles, Birdy, Bugs
    return Animal.query.filter((Animal.birth_year.isnot(None)) & (Animal.birth_year > 2015)).all()

def q4():
    """Return the humans with first names that start with 'J'."""

    # SQL confirmed against database.sql visual check and terminal db query. Watch out for quotes that become backticks.

    # return SELECT fname, lname FROM humans WHERE fname LIKE 'J%';

    # Estimated SQLAlchemy version. Note no ;
    # More at https://docs.sqlalchemy.org/en/13/orm/query.html
    # Sample from docs which has search bar
    # q = session.query(User).filter(User.name.like('e%')).\
    # limit(5).from_self().\
    # join(User.addresses).filter(Address.email.like('q%'))

    # Estimated SQLALchemy Query Employee.query.filter(Employee.name.like('%Jane%')) 

    return Human.query.filter(Human.fname.like('J%')).all()


def q5():
    """Return all animals whose birth years are NULL in the database."""

    # confirmed against database.sql visual check and terminal db query

    # SQL return SELECT name FROM animals WHERE birth_year IS NULL;

    # SQLALchemy Lecture sample return  Employee.query.filter(Employee.state == None) 

    # Bubbles, Mr. Hops,Cuddles

    return Animal.query.filter(Animal.birth_year == None).all() 

def q6():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    # SQL was confirmed against database.sql visual check and terminal db query. Watch out for quotes that become backticks.
     # parallel
     # SQLAlchemy lecture Employee.query.filter(Employee.state.in_(['CA', 'OR']))   # IN ()
     # Bubbles, Mr. Hops, Bugs
    return Animal.query.filter(Animal.animal_species.in_(['fish', 'rabbit'])).all()   # IN ()


def q7():
    """Return all humans whose email addresses do NOT contain 'gmail'."""

    # confirmed against database.sql visual check and terminal db query. Watch out for quotes that become backticks.

    # return SELECT fname, lname FROM humans WHERE email NOT LIKE '%gmail%';

    # guessed based on like in lecture
    
    # Bob Personne
# updated
    return Human.query.filter(Human.email.notlike('%gmail%')).all()

##############################################################################
# PART 3: NAVIGATING RELATIONSHIPS

# **Use SQLAlchemy relationships for each function**
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# app = Flask(__name__)
# app.secret_key = "SECRET"
# def connect_to_db(app, db_name):
#     """Connect to database."""

#     app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{animals}"
#     app.config["SQLALCHEMY_ECHO"] = True
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     db.app = app
#     db.init_app(app)
    
# connect_to_db(app, "animals")
# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.
#
#    The output should look like this (with tabs to indent each animal name under
#    a human's name)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """Print Owner of animls and their species."""

# Replace this with your code fname, lname from humans and name, animal_species joined using foreign key human_id on both tables
# From second lecture
# emps = Employee.query.options(db.joinedload('dept')).all()
# result
# humans = Human.query.options(db.joinedload('human_id')).all() - this join requires a relationship
# printed as text for number of animals. Try again.
# option 2
# #emps = db.session.query(Employee.name,
#                         Department.dept_name,
#                         Department.phone).join(Department).all()

# for name, dept_name, phone in emps:      # [(n, d, p), (n, d, p)]
#     print(name, dept_name, phone)
# Better
# Mess around with formatting
#"{:8} {:11} {:14} {}".format()
# note there must be curly braces for each field and that includes any special thing you do to 
# break out the pets visually such as adding a - or a space or > sign


    humans = db.session.query(Human.fname,
                        Human.lname,
                        Animal.name,
                        Animal.animal_species).join(Animal).all()

    
    for fname, lname, name, animal_species in humans:    
            print("{:8} {:11}".format(fname, lname))
            print("{:8} {:11} {}".format(">", name, animal_species))
# 2. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.
# call in interactive python 
# print_directory()

def find_humans_by_animal_species(species):
    """Enter the species you want to search for in single quotes."""

    # Replace this with your code  animal_species returning fname, lname of human joined using foreign key; filter by

    # SQL SELECT fname, lname, name, animal_species from animals JOIN humans on humans.human_id=animals.animal_id;
    """Show all employees, even those without a dept."""

    # species will be the filter

    # spec = Animal.query.get(species)
    # animals = db.session.query(Human.fname,
    #                     Human.lname,
    #                     Animal.name,
    #                     Animal.animal_species).join(Humans).all()

    
    # for fname, lname, name, animal_species in animals:    
    #         print("{:8} {:11}".format(fname, lname))
    #         print("{:8} {:11} {}".format(">", name, animal_species))

    # test find_humans_by_animal_species('fish')

if __name__ == "__main__":
    from server import app
    from model import connect_to_db

    connect_to_db(app)
