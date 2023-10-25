'''
This module contains the db models
'''
from . import db

class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(50), nullable=False, index=False, unique=False)
    last_name: str = db.Column(db.String(50), nullable=False, index=True, unique=False)
    email: str = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password: str = db.Column(db.String(128))
    notes = db.relationship('Note')
    def __repr__(self) -> str:
        '''
        A method for returning the User model as a string with is first name, last name and email
        '''
        return '<User ID>: {}\n<Username>: {} {}\n<User Email>: {} '.format(self.id, self.first_name, self.last_name, self.email)

class Note(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    content: str = db.Column(db.String(1024), nullable=False, index=False, unique=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self) -> str:
        '''
        A methods for returning the note as a string to print it into the  console
        '''
        return '<Note id> : {}'.format(self.id)
        