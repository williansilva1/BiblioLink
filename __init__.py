from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)

app.config.from_object('config')
bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)

#PAdrão - Tratativa de login_manager do flask
login_manager.init_app(app)
login_manager.login_view = "page_login"
login_manager.login_message = "Acesso negado! Por favor se autentique e tente novamente."
login_manager.login_message_category = "danger"

from .models import cliente_model, funcionario_model,livro_model,venda_model

from .routes import home_routes, livro_routes,  venda_routes, cliente_routes, funcionario_routes
