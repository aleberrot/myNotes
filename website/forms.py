'''
This module is for creating the forms classes
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from .models import User

class LoginForm(FlaskForm):
    '''
    This LoginForm class inherits from FlaskForm and its usage is for creating the application login form.
    '''
    email: str = StringField('E-mail', validators=[DataRequired(), Email()]) # Creating a label for the email
    password: str = StringField('Password', validators=[DataRequired()]) # Creating a label for the password
    remember_me: bool = BooleanField('Remember me')
    submit = SubmitField('Submit!')

class RegisterForm(FlaskForm):
    '''
    This let register users
    '''
    def validate_email(self, email_to_check: str):
        '''
        This method checks if there is an user with the given email and raises an error if it is
        '''
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Already a user with that E-mail! try a new one')
        return True

    first_name: str = StringField('First Name', validators=[DataRequired(), Length(min=4, max=45)])
    last_name: str = StringField('Last Name', validators=[DataRequired(), Length(min=4, max=48)])
    email: str = StringField('E-mail', validators=[DataRequired(), Email()])
    password: str = StringField('Password', validators=[DataRequired(), Length(min=8)])
    password2: str = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

class NoteForm(FlaskForm):
    '''
    Lets the user creates notes 
    '''
    note_content: str = StringField('Note Content', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Create Note')
