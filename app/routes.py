from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

#this is a the main view function 
def index():
    user = {'username': 'Vajo'}

    posts = [
        {
            'author': {'username': 'JohnWick'},
            'body': 'The weather in Rome is wicked!'
        },
        {
            'author': {'username': 'LenaHeadey'},
            'body': 'The love movie was so sweet!'
        },
        {
            'author': {'username': 'KasperSchmeichel'},
            'body': 'The laser was no factor at all!'
        },
        {
            'author': {'username': 'JohnWick'},
            'body': 'The weather in Rome is wicked!'
        },
        {
            'author': {'username': 'LenaHeadey'},
            'body': 'The love movie was so sweet!'
        },
        {
            'author': {'username': 'KasperSchmeichel'},
            'body': 'The laser was no factor at all!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)