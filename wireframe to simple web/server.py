"""Server for checklist app."""

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
            # session['user-id']=user_id
            # user_id=session['user_id']
            return render_template('/homepage.html')
        else:
            flash('Please re-enter your password')
            return render_template('/login.html')
    else:
        crud.create_user(email, password,user_full_name)
        flash('Account created!')
        # session['user-id']=user_id
        # user_id=session['user_id']
        return render_template('/login.html')
        
# app route for all templates
@app.route('/templates')
def all_templates():
    """View all templates."""

    templates = crud.get_templates()
    users=crud.get_users()
    return render_template('all_templates.html', templates=templates, users=users)

# app route for template details
@app.route('/templates/<template_id>')
def show_template(template_id):
  #Show details on a particular template.

    template = crud.get_template_by_id(template_id)
    users=crud.get_users()
    # isnotcreator=template.created_by!=session.get("user_id")
    return render_template('template_details.html', template=template, users=users)

@app.route('/createtemplate', methods=['POST'])
def createtemplate():
    """Create new template."""

    template_name = request.form.get('template_name')
    created_by = request.form.get('created_by')
    created_on = request.form.get('created_on')

    crud.create_template(template_name, created_by, created_on)
    flash('Template created!')
    templates = crud.get_templates()
    users=crud.get_users()
    return render_template('/all_templates.html', templates=templates, users=users)

@app.route('/createquestion', methods=['POST'])
def createquestion():
    """Create new question."""

    template_id = request.form.get('template_id')
    question = request.form.get('question')
    yes_text =request.form.get('yes_text')
    no_text = request.form.get('no_text')
    not_applicable_text = request.form.get('not_applicable_text')
    category = request.form.get('category')
    primary_driver = request.form.get('primary_driver')
    resource_url = request.form.get('resource_url')
    help_text = request.form.get('help_text')

    crud.create_question(template_id, question, yes_text, no_text, not_applicable_text, category, primary_driver, resource_url, help_text)
    
    flash('Question added!')

    questions = crud.get_questions()
    templates = crud.get_templates()
    users=crud.get_users()
    return render_template('/all_templates.html', templates=templates, questions=questions, users=users)


@app.route('/questions')
def all_questions():
    """View all questions."""

    questions = crud.get_questions()

    return render_template('all_questions.html', questions=questions)

@app.route('/questions/<question_id>')
def show_question(question_id):
  #Show details on a particular question.
    question = crud.get_question_by_id(question_id)

    return render_template('question_details.html', question=question)
    
# app route for all checklists
@app.route('/checklists')
def all_checklists():
    """View all checklists."""

    checklists = crud.get_checklists()
    users=crud.get_users()
    return render_template('all_checklists.html', checklists=checklists, users=users)

@app.route('/checklists/<checklist_id>')
def show_checklist(checklist_id):
  #Show details on a particular template.
    checklist = crud.get_checklist_by_id(checklist_id)
    users=crud.get_users()
    answers=crud.get_answers()
    return render_template('checklist_details.html', checklist=checklist, users=users, answers=answers)

@app.route('/createchecklist', methods=['POST'])
def createchecklist():
    """Create new checklist."""
    template_id = request.form.get('template_id')
    who_for = request.form.get('who_for')
    time_frame = request.form.get('time_frame')
    preparer = request.form.get('preparer')
    reviewer = request.form.get('reviewer')

    crud.create_checklist(template_id,  who_for, time_frame, preparer, reviewer)
    flash('Checklist created!')
    
    checklists = crud.get_checklists()
    users=crud.get_users()
    return render_template('/all_checklists.html', checklists=checklists, users=users)

@app.route('/answers')
def all_answers():
    """View all answers."""

    answers = crud.get_answers()

    return render_template('all_answers.html', answers=answers)

@app.route('/answers/<answer_id>')
def show_answer(answer_id):
  # Show details on a particular answer.
    answer = crud.get_answer_by_id(answer_id)

    return render_template('answer_details.html', answer=answer)

@app.route('/createprepareranswer', methods=['POST'])

def createprepareranswer():
    """Create new preparer answer."""

    checklist_id = request.form.get('checklist_id')
    question_id = request.form.get('question_id')
    preparer_answer = request.form.get('preparer_answer')
    preparer_time = request.form.get('preparer_time')
    preparer_comment = request.form.get('preparer_comment')
    
    crud.create_prepareranswer(checklist_id, question_id, preparer_answer, preparer_time, preparer_comment)
    flash('Preparer answer posted! Select checklist.')
    checklists = crud.get_checklists()
    return render_template('all_checklists.html', checklists=checklists)

@app.route('/creatreviewereanswer', methods=['POST'])

def createrevieweranswer():
    """Create new reviewer answer."""

    checklist_id = request.form.get('checklist_id')
    question_id = request.form.get('question_id')
    reviewer_ready = request.form.get('reviewer_ready')
    reviewer_time = request.form.get('reviewer_time')
    reviewer_comment = request.form.get('reviewer_comment')
    
    crud.create_revieweranswer(checklist_id, question_id, reviewer_ready, reviewer_time, reviewer_comment)
    flash('Reviewer answer posted! Select checklist.')
    checklists = crud.get_checklists()
    return render_template('all_checklists.html', checklists=checklists)

@app.route('/chooserecipient', methods=['POST'])

def chooserecipient():
    """Choose pre-existing recipient."""

    checklist_id = request.form.get('checklist_id')
    recipient_id = request.form.get('recipient_id')

    crud.choose_recipient(checklist_id, recipient_id)
    flash('Recipient attached to checklist!')
    checklists = crud.get_checklists()
    return render_template('/all_checklists.html', checklists=checklists)

@app.route('/registerrecipient', methods=['POST'])

def register_recipient():
    """Create a new recipient user."""
    

    user_full_name = request.form.get('user_full_name')

    email = request.form.get('email')

    password = request.form.get('password')

    crud.create_recipient(user_full_name, email, password)
    
    flash('Account created!')
    checklists = crud.get_checklists()
    users=crud.get_users()
    return render_template('all_checklists.html', users=users, checklists=checklists)

@app.route('/markcomplete', methods=['POST'])

def markcomplete():
    """Mark checklist complete."""

    checklist_id = request.form.get('checklist_id')
    date_complete = request.form.get('date_complete')
    
    crud.mark_complete(checklist_id, date_complete)
    flash('Checklist marked complete! Select checklist desired.')
    checklists = crud.get_checklists()
    return render_template('all_checklists.html', checklists=checklists)

@app.route('/markdatesenttoreview', methods=['POST'])

def markdatesenttoreview():
    """Mark date sent to review."""

    checklist_id = request.form.get('checklist_id')
    date_sent_to_review = request.form.get('date_sent_to_review')
    
    crud.mark_datesenttoreview(checklist_id, date_sent_to_review)
    flash('Date sent to review registered! Select checklist desired.')
    checklists = crud.get_checklists()
    return render_template('all_checklists.html', checklists=checklists)

@app.route('/markdatereviewcompleted', methods=['POST'])

def markdatereviewcompleted():
    """Mark date review completed."""

    checklist_id = request.form.get('checklist_id')
    date_review_completed = request.form.get('date_review_completed')
    
    crud.mark_datereviewcompleted(checklist_id, date_review_completed)
    flash('Date review completed registered! Select checklist desired.')
    checklists = crud.get_checklists()
    return render_template('all_checklists.html', checklists=checklists)

if __name__ == '__main__':
# added connection to database
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
