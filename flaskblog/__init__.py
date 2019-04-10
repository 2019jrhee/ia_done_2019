from flask import Flask
# application for the database
from flask_sqlalchemy import SQLAlchemy

# application for encrypting the password
from flask_bcrypt import Bcrypt

#application for user logging in
from flask_login import LoginManager

app = Flask(__name__)
#for security
app.config['SECRET_KEY'] = '0688991dd4efef8f189cf116e83258ef'

# database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#for password hash
bcrypt = Bcrypt(app)

#for login function for the user
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# for login flash message
login_manager.login_message_category = 'info'

# import all the routes from routes.py to run
from flaskblog import routes
