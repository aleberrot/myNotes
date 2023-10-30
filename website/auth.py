'''
Creating the blueprints for the authtentication routes
'''
from flask import Blueprint, render_template, url_for, redirect, flash
from . import db # Importing the database
from .forms import LoginForm, RegisterForm # Importing the forms classes
from .models import User # Importing our db models 
from flask_login import login_user, logout_user

auth: Blueprint = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    A function for loggin in the user to the website
    '''
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        # Comprobates if the user exists
        user_attempt = User.query.filter_by(email=form.email.data).first()
        if user_attempt and user_attempt.check_password(password_to_check=form.password.data):
            login_user(user_attempt)
            flash(f'Success! You are logged in {user_attempt.first_name}', category='success') 
            return redirect(url_for('views.index'))

        else:
            flash('E-mail or password do not match, try again!', category='danger')
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Error: {error_message}', category='danger')
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    This function is for registrating the users
    '''
    form: RegisterForm = RegisterForm()
    if form.validate_on_submit(): # Never forget parenthesis
        new_user: User = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password_hash=form.password.data)
        db.session.add(new_user)
        db.session.commit() 
        flash('User created successfully', category='success')
        return redirect(url_for('auth.login'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Error: {error_message}', category='danger')

    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    '''
    Let the users logout from the page
    '''
    # Logout the user and redirects it to the register
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('auth.register'))