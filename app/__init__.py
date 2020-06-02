from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from .config import config_settings


db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config_settings['development'])
db.init_app(app)
migrate.init_app(app, db)

from . import routes, models, schema
