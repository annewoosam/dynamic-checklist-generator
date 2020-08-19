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
@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/template/<int:template_id>')
def get_template(template_id):
    """Return a template from the database as JSON."""

    template = Template.query.get(template_id)

    if template:
        return jsonify({'status': 'success',
                        'template_id': template.template_id,
                        'templatename': template.templatename,
                        'createdby': template.createdby,
                        'createdon': template.createdon})
    else:
        return jsonify({'status': 'error',
                        'message': 'No template found with that ID'})


#     @app.route('/')
# def homepage():
#     """View homepage."""

#     return render_template('login.html')

# @app.route('/users')
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users)

# @app.route('/register', methods=['POST'])

# def register_user():
#     """Create a new user."""

#     email = request.form.get('email')
#     password = request.form.get('password')

#     user = crud.get_user_by_email(email)
#     passwd = crud.get_user_by_password(password)

#     if user:
        
#         if passwd:
#             ('Log-in successful...')
#             return render_template('/homepage.html')
#         else:
#             flash('Please re-enter your password')
#             return render_template('/login.html')
#     else:
#         crud.create_user(email, password)
#         flash('Account created! Please log in.')
#         return render_template('/login.html')

# @app.route('/users/<user_id>')
# def user_details(user_id):
#     """View all users."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

# # app route for all templates
# @app.route('/templates')
# def all_templates():
#     """View all templates."""

#     templates = crud.get_templates()

#     return render_template('all_templates.html', templates=templates)

# # app route for template questions(details)
# @app.route('/templates/<template_id>')
# def show_template_questions(template_id):
#   #Show question details for a particular template.

#     template = crud.get_template_by_id(template_id)

#     return render_template('template_questions_details.html', template=template)


if __name__ == '__main__':
# added connection to database
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
