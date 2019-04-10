# importing forms from Flask WTForms
from flask_wtf import FlaskForm
# importing writing fields from Flask WTForms
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
# importing class User from models.py for RegistrationForm and LoginForm
from flaskblog.models import User

# components for registering / user input for all the components is needed
class RegistrationForm(FlaskForm):
	# length of the username is 5-20 letters when creating an account
	username = StringField('Username',
		validators= [DataRequired(), Length(min=5, max=20)])
	# requiring the user input
	email = StringField('Email', validators= [DataRequired(), Email()])

	password = PasswordField('Password', validators= [DataRequired()])

	submit = SubmitField('Register')



# components for logging in / user input for all the components is needed
class LoginForm(FlaskForm):
	# length of the username is 5-20 letters when logging into an account
	username = StringField('Username',
		validators= [DataRequired(), Length(min=5, max=20)])
	# requiring the user input
	password = PasswordField('Password', validators= [DataRequired()])

	submit = SubmitField('Log In')


# components for creating posts / user input for all the components is needed
class PostForm(FlaskForm):
	# length of the title is 5-50 letters when creating a post
	title = StringField('Title', validators=[DataRequired(), Length(min=5, max=50)])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
