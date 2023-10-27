'''
Creating blueprints for the navigable routes
'''
from flask import Blueprint, render_template, url_for, redirect
from .forms import NoteForm

views: Blueprint = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    '''
    A home page where the user can see their notes and create new ones
    '''
    form: NoteForm = NoteForm()
    return render_template('home.html', form=form)

