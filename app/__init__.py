import os
import secrets
from dotenv import load_dotenv
from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from app.database import db_session, init_db
from config import connection_string
from app import models

load_dotenv()

app = Flask(__name__)
app.logger.info('Environmental variable Initialized')
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

with app.app_context():
    init_db()


secret_key = os.getenv("SECRET_KEY", secrets.token_urlsafe(16))
app.config['SECRET_KEY'] = secret_key
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)

from app import routes, models

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()    




