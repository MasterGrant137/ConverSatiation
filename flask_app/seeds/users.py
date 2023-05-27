"""Users seed."""

from models import db, User
from faker import Faker

fake = Faker()

def seed_users():
    """Seed the users."""
    johnny_appleseed = User(username='Johnny Appleseed', email='jseed@email.com', password='password')
    db.session.add(johnny_appleseed)

    demo = User(username='Demo', email='demo@email.com', password='password')
    db.session.add(demo)

    db.session.commit()

def undo_users():
    """Undo users seed.
    
    `TRUNCATE` removes all the data from the table,
    `RESET IDENTITY` resets the auto incrementing primary key,
    `CASCADE` deletes any dependent entities.
    """
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
