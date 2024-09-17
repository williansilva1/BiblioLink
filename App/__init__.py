from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from importlib import import_module


db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)

app.config.from_object('config')
bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)

#Padrão - Tratativa de login_manager do flask
login_manager.init_app(app)
login_manager.login_view = "page_login"
login_manager.login_message = "Acesso negado! Por favor se autentique e tente novamente."
login_manager.login_message_category = "danger"

#Biblioteca do Python para importações
modules = ('cliente', 'funcionario', 'livro', 'home', 'venda')
for module_name in modules:
    module = import_module('App.{}.routes'.format(module_name))
    app.register_blueprint(module.blueprint)

