"""User model."""

from datetime import datetime
from flask_app.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """User model class.

    Since User is passed to flask_login at the login route,
    these methods are available on current_user.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @property
    def password(self):
        """Password definition."""
        return self.hashed_password
    
    @password.setter
    def password(self, password):
        """Hash and salt password."""
        self.hashed_password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against salted and hashed password."""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Make selected columns into dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }