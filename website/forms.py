'''
This module is for creating the forms classes
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

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
    first_name: str = StringField('First Name', validators=[DataRequired()])
    last_name: str = StringField('Last Name', validators=[DataRequired()])
    email: str = StringField('E-mail', validators=[DataRequired(), Email()])
    password: str = StringField('Password', validators=[DataRequired()])
    password2: str = StringField('Confirm Password', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Create Account')