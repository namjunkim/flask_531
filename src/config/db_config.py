from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()
# Configure the app with the database URI
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your_database'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
