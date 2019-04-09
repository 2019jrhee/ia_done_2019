from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from flaskblog.models import User

# components for registering
class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators= [DataRequired(), Length(min=5, max=20)])
	email = StringField('Email', validators= [DataRequired(), Email()])

	password = PasswordField('Password', validators= [DataRequired()])

	submit = SubmitField('Register')


# components for logging in
class LoginForm(FlaskForm):
	username = StringField('Username',
		validators= [DataRequired(), Length(min=5, max=20)])


	password = PasswordField('Password', validators= [DataRequired()])


	submit = SubmitField('Log In')

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
