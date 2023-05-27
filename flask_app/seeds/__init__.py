"""CLI seed commands.

They can be viewed by `flask seed --help`.
"""

from flask.cli import AppGroup
from .users import seed_users, undo_users


seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    """Create the `flask seed all` command."""
    seed_users()

@seed_commands.command('undo')
def undo():
    """Create the `flask seed undo` command."""
    undo_users()