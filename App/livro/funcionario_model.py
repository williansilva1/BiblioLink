from App import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Funcionario.query.get(int(user_id))

class Funcionario(db.Model, UserMixin):
    __tablename__ = "funcionarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    #nome, cpf, salario, cargo, setor
    nome=db.column(db.String(40), nullable=False )
    cpf=db.column(db.String(14), unique=True, nullable=False)
    salario=db.column(db.float(2), nullable=False)
    cargo=db.column(db.String(20), nullable=False)
    setor=db.column(db.String(20), nullable=False)
    login=db.column(db.String(20), nullable=False)
    senha=db.column(db.String(255), nullable=False)
    
    def encriptar_senha(self):
        self.senha = bcrypt.generate_password_hash(self.senha).decode('utf-8')

    def validar_senha(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)
    
    def __repr__(self):
        return str(self.id) + " - " + self.nome