from flask import Flask
from src.config.db_config import db, migrate
from src.config.config import config

def create_app(env):
    app = Flask('531 Project')
    app.config.from_object(config[env])
    db.init_app(app)
    migrate.init_app(app, db)
    return app