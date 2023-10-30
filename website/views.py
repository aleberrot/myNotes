'''
Creating blueprints for the navigable routes
'''
from . import db
from flask import Blueprint, render_template, url_for, redirect, flash, request
from .forms import NoteForm
from flask_login import login_required, current_user
from .models import Note

views: Blueprint = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    '''
    A home page where the user can see their notes and create new ones
    '''
    form: NoteForm = NoteForm()
    if form.validate_on_submit():
        new_note: Note = Note(content=form.note_content.data, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note successfully added!', category='success')
    else:
        flash('Make sure that your note has at least one character', category='warning')
    return render_template('home.html', form=form)

@views.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    '''
    This route is for deleting the note that the user wants to 
    '''
    try:
        note_to_delete = Note.query.get_or_404(id)
        db.session.delete(note_to_delete)
        db.session.commit()
        flash('Note deleted', category='success')
    except:
        flash('An error ocurred while deleting the note', catogory='alert')
    return redirect(url_for('views.index'))