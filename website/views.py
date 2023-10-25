'''
Creating blueprints for the navigable routes
'''
from flask import Blueprint, render_template, url_for, redirect

views: Blueprint = Blueprint('views', __name__)

@views.route('/')
def index():
    '''
    '''
    return render_template('home.html')

