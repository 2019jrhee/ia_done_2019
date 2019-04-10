# import timestamp function for the posted date
from datetime import datetime
# import database and login_manager from the project folder
from flaskblog import db, login_manager
# import UserMixin, default login implementation
from flask_login import UserMixin


#login_manager extension decorator @
@login_manager.user_loader
def load_user(user_id):
	# get everything from the database with the user_id when logging in
	return User.query.get(int(user_id))

# database setup
class User(db.Model, UserMixin):
	# following unique components will be saved in the database
	id = db.Column(db.Integer, primary_key=True)
	# the username must be different from an existing username in the database
	username = db.Column(db.String(15), unique=True, nullable=False)
	# the email must be different from an existing email in the database
	email = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)

	# get the author who created the post in the Post model
	posts = db.relationship('Post', backref='author', lazy=True)

	# show the username, email and password in the database
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}')"

class Post(db.Model):
	# following unique components will be saved in the database
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	content = db.Column(db.Text, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	# show the post title and date in the database
	def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
