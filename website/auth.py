'''
Creating the blueprints for the authtentication routes
'''
from flask import Blueprint, render_template, url_for, redirect, flash
from .forms import LoginForm, RegisterForm # Importing the forms classes

auth: Blueprint = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    A function for loggin in the user to the website
    '''
    form: LoginForm = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    This function is for registrating the users
    '''
    form: RegisterForm = RegisterForm()
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    '''
    '''
    return 'Logout' 