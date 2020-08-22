"""Server for movie ratings app."""

# increased flask
from flask import Flask, render_template, request, flash, session, jsonify, redirect

# created import allowing connection to database
from model import connect_to_db, Template

# imported module to allow to create,read,update and delete database
import crud

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# created basic homepage route at index
# @app.route('/')
# def homepage():
#     """Show the homepage."""

#     return render_template('index.html')


# this works in separate project to push own data through/clone and get to work for pieces/ saved as separtae project databridgeoriginal


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('login.html')

@app.route('/register', methods=['POST'])

def register_user():
    """Create a new user."""

    user_full_name = request.form.get('user_full_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    passwd = crud.get_user_by_password(password)

    if user:
        
        if passwd:
            ('Log-in successful...')
            return render_template('/homepage.html')
        else:
            flash('Please re-enter your password')
            return render_template('/login.html')
    else:
        crud.create_user(email, password,user_full_name)
        flash('Account created!')
        return render_template('/login.html')
        
# @app.route('/users')
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users)

# @app.route('/users/<user_id>')
# def user_details(user_id):
#     """View all users."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

# app route for all templates
@app.route('/templates')
def all_templates():
    """View all templates."""

    templates = crud.get_templates()

    return render_template('all_templates.html', templates=templates)

@app.route('/checklists')
def all_checklists():
    """View all checklists."""

    checklists = crud.get_checklists()

    return render_template('all_checklists.html', checklists=checklists)

@app.route('/questions')

def all_questions():
    """View all questions."""

    questions = crud.get_questions()

    return render_template('all_questions.html', questions=questions)

@app.route('/answers')
def all_answers():
    """View all answers."""

    answers = crud.get_answers()

    return render_template('all_answers.html', answers=answers)

# app route for template details
@app.route('/templates/<template_id>')
def show_template(template_id):
  #Show details on a particular template.

    template = crud.get_template_by_id(template_id)

    return render_template('template_details.html', template=template)

# @app.route('/api/templates/<int:template_id>')
# def get_template(template_id):
#     """Return a template from the database as JSON."""

#     template = Template.query.get(template_id)

#     if template:
#         return jsonify({'status': 'success',
#                         'template_id': template.template_id,
#                         'templatename': template.templatename,
#                         'createdby': template.createdby,
#                         'createdon': template.createdon})
#     else:
#         return jsonify({'status': 'error',
#                         'message': 'No template found with that ID'})

if __name__ == '__main__':
# added connection to database
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
