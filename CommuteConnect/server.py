from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY']='37d7957f5f28dc3eaaca2ff0698fdd09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    password = db.Column(db.String(60), nullable=False)

    rides = db.relationship('Post', backref='driver', lazy=True)



    def __repr__(self):

        return f"User('{self.username}', '{self.email}', '{self.image_file}')"





class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    departure = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    destination = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



    def __repr__(self):

        return f"Post('{self.title}', '{self.date_posted}')"

rides = [

    {

        'driver': 'Corey Schafer',

        'title': 'Entreprneur',

        'destination': 'Austin Tx',

        'departure': 'April 20, 2018'

    },

    {

        'driver': 'Mak Taylor',

        'title': 'Investor',

        'destination': 'San Antonio Tx',

        'departure': 'April 22, 2018'

    }

]
@app.route("/")
@app.route("/home")
def home():
    return render_template('profile.html')

@app.route("/profile")

def profile():
    return render_template('TejanoTech.html', rides=rides)
@app.route("/ride")
def ride():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])

def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        flash(f'Account created for {form.username.data}!', 'success')

        return redirect(url_for('profile'))

    return render_template('register.html', title='Register', form=form)
@app.route('/about')
def about():
    return render_template('fakepost.html')

@app.route("/login", methods=['GET', 'POST'])

def login():

    form = LoginForm()

    if form.validate_on_submit():

        if form.email.data == 'admin@blog.com' and form.password.data == 'password':

            flash('You have been logged in!', 'success')

            return redirect(url_for('profile'))

        else:

            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':

    app.run(debug=True)
