"""Use Skills 5: SQLAlchemy & AJAX to construct queries

"""
from flask_sqlalchemy import SQLAlchemy

from model import db, #add relevant modelClasses. Sample SQLAlchemt queries below for now

def q1():
 
    return Human.query.filter(Human.human_id == 2).all()

def q2():

    return Animal.query.filter(Animal.animal_species == 'fish').one()   

def q3():

    return Animal.query.filter((Animal.birth_year.isnot(None)) & (Animal.birth_year > 2015)).all()

def q4():

    return Human.query.filter(Human.fname.like('J%')).all()


def q5():

    return Animal.query.filter(Animal.birth_year == None).all() 

def q6():

    return Animal.query.filter(Animal.animal_species.in_(['fish', 'rabbit'])).all()   # IN ()


def q7():

    return Human.query.filter(Human.email.notlike('%gmail%')).all()

def print_directory():

    humans = db.session.query(Human.fname,
                        Human.lname,
                        Animal.name,
                        Animal.animal_species).join(Animal).all()

    
    for fname, lname, name, animal_species in humans:    
            print("{:8} {:11}".format(fname, lname))
            print("{:8} {:11} {}".format(">", name, animal_species))

def find_humans_by_animal_species(species):

    animals = Animal.query.filter(Animal.animal_species == species)\
                          .options(db.joinedload('human'))\
                          .all()

    unique_humans = set([animal.human for animal in animals])

    return list(unique_humans)
    
if __name__ == "__main__":
    from server import app
    from model import connect_to_db

    connect_to_db(app)
