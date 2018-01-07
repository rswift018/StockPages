import uuid

from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

@app.route('/')
def index():
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.valid_login(email, password):
        User.login(email)

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run()
