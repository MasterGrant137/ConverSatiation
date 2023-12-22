"""App configuration."""

import os
from dotenv import load_dotenv


load_dotenv()

class Config:
        """Configuration class."""

        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        SQLALCHEMY_TRACK_MODIFICATION = False
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
        SQLALCHEMY_ECHO = True
