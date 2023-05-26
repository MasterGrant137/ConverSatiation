"""Auth routes."""

from flask import Blueprint, request
from models import db
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
          return { 'errors': ['Unauthorized'] }
     
@auth_routes.route('signup')
def authenticateSignup():
     """Authenticate user signup."""
     if current_user.is_authenticated:
          return current_user.to_dict()
     return { 'errors': ['Unauthorized'] }

@auth_routes.route('/login', methods=['POST'])
def login():
     """Log a user in. Give context to flask_login."""
    #  form = 