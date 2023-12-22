"""Auth routes."""

from flask import Blueprint, request
from forms.login_form import LoginForm
from forms import LoginForm, SignupForm
from models import db, User
from flask_login import current_user, login_user, logout_user

auth_routes = Blueprint('auth', __name__)

def validation_errors_to_error_messages(validation_errors: list[dict]) -> list[str]:
    """Turn the WTForms validation error into a simple list."""
    errorMessages = []
    for field in validation_errors:
            for error in validation_errors[field]:
                errorMessages.append(error)
    return errorMessages

@auth_routes.route('/login')
def authenticateLogin():
    """Authenticate user login."""
    if current_user.is_authenticated:
        return current_user.to_dict()
    return { 'errors': ['Unauthorized'] }

@auth_routes.route('/signup')
def authenticateSignup():
    """Authenticate user signup."""
    if current_user.is_authenticated:
        return current_user.to_dict()
    return { 'errors': ['Unauthorized'] }

@auth_routes.route('/login', methods=['POST'])
def login():
    """Log a user in. Give context to flask_login."""
    form = LoginForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return { 'errors': validation_errors_to_error_messages(form.errors) }, 401

@auth_routes.route('/logout')
def logout():
    """Log out a user."""
    logout_user()
    return { 'message': 'User logged out.' }

@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """Create a new user and log that user in."""
    form = SignupForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return { 'errors': validation_errors_to_error_messages(form.errors) }, 401
