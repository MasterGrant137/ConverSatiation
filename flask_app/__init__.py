"""Flask initialization."""

import os
from flask import Flask, request, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import generate_csrf
from flask_login import LoginManager
from routes import auth_routes

from .models import db, User

from .seeds import seed_commands

from .config import Config

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_user(id):
    """Load a user from session."""
    return User.query.get(int(id))

app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(auth_routes, url_prefix='/api/auth')

db.init(app)
Migrate(app, db)

CORS(app)

@app.before_request
def https_redirect():
    """Assure, in production, that requests made over HTTP are redirected to HTTPS."""
    if os.environ.get('FLASK_ENV') == 'production':
            if request.headers.get('X-Forwarded-Proto') == 'http':
                 url = request.url.replace('http://', 'https//:', 1)
                 moved_permanently_status_code = 301
                 return redirect(url, code=moved_permanently_status_code)
            
@app.after_request
def inject_csrf_token(response):
    """Set cross-site request forgery (CSRF) token.

    If a user clicks on a malicious link while logged into an unprotected site,
    a bad actor can exploit the fact that a session token is active and send a
    POST request to that site, acting as the user. To protect against this, a random
    and unique token is generated upon each HTTP request. It is a shared secret between
    the client and the server and thus prevents the bad actor from successfully imitating the
    user through a POST request alone.

    Setting the SameSite attribute to strict on the cookie assures that the cookie is only
    included in requests made on the site which prevents the authentication of requests made
    off the site. There is also the option of setting it to lax which includes the cookie only
    if the request is a GET and initiated by the user, not a script.
    """
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
             'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
     """Serve static React app files."""
     if path == 'favicon.ico':
          return app.send_static_file('favicon.ico')
     return app.send_static_file('index.html')
