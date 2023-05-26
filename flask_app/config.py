"""App configuration."""

import os

class Config:
        """Configuration class."""

        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_TRACK_MODIFICATION = False
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        SQLALCHEMY_ECHO = True
