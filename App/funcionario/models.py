from App import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Funcionario.query.get(int(user_id))

class Funcionario(db.Model, UserMixin):
    __tablename__ = "funcionarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    #nome, cpf, salario, cargo, setor, login, senha
    nome=db.Column(db.String(40), nullable=False )
    cpf=db.Column(db.String(14), unique=True, nullable=False)
    salario=db.Column(db.Float(2), nullable=False)
    cargo=db.Column(db.String(20), nullable=False)
    setor=db.Column(db.String(20), nullable=False)
    login=db.Column(db.String(20), nullable=False)
    senha=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Funcionario {self.nome}>' #str(self.id) + " - " + self.nome