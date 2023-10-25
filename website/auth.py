'''
Creating the blueprints for the authtentication routes
'''
from flask import Blueprint, render_template, url_for, redirect, flash
from . import db # Importing the database
from .forms import LoginForm, RegisterForm # Importing the forms classes
from .models import User, Note # Importing our db models 

auth: Blueprint = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    A function for loggin in the user to the website
    '''
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        # Comprobates if the user exists
        return redirect(url_for('views.index'))
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    This function is for registrating the users
    '''
    form: RegisterForm = RegisterForm()
    if form.validate_on_submit():
        new_user: User = User()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    '''
    '''
    return 'Logout' 