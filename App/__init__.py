from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

from .models import livro_model

from .routes import home_routes, livro_routes