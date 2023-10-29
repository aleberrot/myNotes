'''
This module contains the db models
'''
from . import db, bcrypt, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
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
    
    @property
    def password_hash(self) -> str:
        '''
        Returns the user's password
        '''
        return self.password
    
    @password_hash.setter
    def password_hash(self, password_text):
        '''
        Generates a hash for the user's password
        '''
        self.password =  bcrypt.generate_password_hash(password_text).decode('utf-8')

    def check_password(self, password_to_check: str) -> bool:
        '''
        Check if the password given matches with the user password
        '''
        return  bcrypt.check_password_hash(self.password, password_to_check)

class Note(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    content: str = db.Column(db.String(1024), nullable=False, index=False, unique=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self) -> str:
        '''
        A methods for returning the note as a string to print it into the  console
        '''
        return '<Note id> : {}'.format(self.id)

@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(int(user_id))