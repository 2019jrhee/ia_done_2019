# import necessary functions from flask
from flask import render_template, url_for, flash, redirect, request
# import application, database and encrypt function from the project folder
from flaskblog import app, db, bcrypt
# import all the Forms from forms.py
from flaskblog.forms import RegistrationForm, LoginForm, PostForm
# import class User and class Post from models.py
from flaskblog.models import User, Post
# import login/logout related functions from flask_login
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")

def home():
	# grabbing all the post from the database
	posts = Post.query.all()
	# link the design of 'home.html' and display all the posts on the home page
	return render_template ('home.html', posts=posts)


# getting user input and save it in database
@app.route("/register", methods=['GET', 'POST'])
def register():
	# if user is already logged in, he/she will be redirected to home page
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	# use the RegistrationForm, which was created in forms.py
	form = RegistrationForm()
	if form.validate_on_submit():
		#hashed password for safety
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password= hashed_pw)
		# add a user with this username, email and password to the database
		db.session.add(user)
		db.session.commit()
		# show the flash message when registration is complete
		flash('Your account has been created! Go ahead and log in!', 'success')
		# send the user to the login page
		return redirect(url_for('login'))
	# link the design of 'register.html' and use the RegistrationForm
	return render_template ('register.html', title= 'Register', form=form)


# checking the user input with database to log in
@app.route("/login", methods=['GET', 'POST'])
def login():
	# if user is already logged in, he/she will be redirected to home page
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	# use the LoginForm in forms.py
	form = LoginForm()

	#checking if the username and password typed match the ones on the database
	if form.validate_on_submit():
		# grabbing the username saved in database
		user = User.query.filter_by(username=form.username.data).first()
		# compares the password typed with the one that matches the username
		# if the username and password match the ones in database, log in the user
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			next_page = request.args.get('next')
			flash('You are successfully logged in!', 'success')
			#if next page exists then redirect to that page, but if not, redirect to the home page
			return redirect(next_page) if next_page else redirect(url_for('home'))

		else:
			# show this flash message when login fails
			flash('Incorrect username or password', 'danger')
	# link the design of 'login.html' and use the LoginForm
	return render_template ('login.html', title= 'Login', form=form)

# users can log out
@app.route("/logout")
def logout():
	# logs out the user
	logout_user()
	# show this flash message when logout succeeds
	flash('You are successfully logged out!', 'success')
	# send the user back to the home page
	return redirect(url_for('home'))

# users can see their account after creating and logging in
@app.route("/account")
# only users who are logged in can access their account page
@login_required
def account():
	# link the design of 'account.html'
	return render_template ('account.html', title= 'Account')

# users can add a new post once they are logged in
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
	# use the PostForm in forms.py
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		# adding the post to the database
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created!', 'success' )
		# go back to homepage once saved
		return redirect(url_for('home'))
	# link the design of 'create_post.html' and use the PostForm
	return render_template ('create_post.html', title= 'New Post', form=form)
