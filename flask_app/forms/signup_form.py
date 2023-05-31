"""Signup form."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_app.models import User
import re

def email_exists(form, field):
    """Check if email is in use."""
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user: raise ValidationError('Email address already in use.')

def username_exists(form, field):
    """Check if username is in use."""
    username = field.data
    user = user.query.filter(User.username == username).first()
    if user: raise ValidationError('Username already in use.')

def proper_password(form, field):
    """Check if password meets character and length requirements.
    
    Runs the user input against regex to see if it has an uppercase
    letter, lowercase letter, symbol, and number. It also determine
    if the length specification (8 characters) is met.
    """
    validation_errors = []
    password = field.data

    lowercase_letter_present = bool(re.search(r'[a-z]', password))
    uppercase_letter_present = bool(re.search(r'[A-Z]', password))
    number_present = bool(re.search(r'[0-9]', password))
    symbol_present = bool(re.search(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\[\{\}\]\\\|\;\:\'\"\,\<\.\>\/\?]', password))

    if not lowercase_letter_present: validation_errors.append('At least one lowercase letter is required in the password.')
    if not uppercase_letter_present: validation_errors.append('At least one uppercase letter is required in the password.')
    if not number_present: validation_errors.append('At least one number is required in the password.')
    if not symbol_present: validation_errors.append('At least one symbol is required in the password.')

    if len(validation_errors): raise ValidationError(' '.join(validation_errors))

class SignupForm(FlaskForm):
    """Signup form class."""

    username = StringField('username', validators=[DataRequired(message='Username is required!'), username_exists])
    email = StringField('email', validators=[DataRequired(message='Email is required!'), email_exists])
    password = PasswordField('password', validators=[Length(min=8, max=255,
        message='Passwords must be between 8 and 255 characters, inclusively!'),
        DataRequired(message='Password is required!'), proper_password])
