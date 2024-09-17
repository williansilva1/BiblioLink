from App import db
from App.livro.models import Livro 
from App.cliente.models import Cliente 
from App.funcionario.models import Funcionario


class Venda(db.Model):
    __tablename__ = "vendas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    dataVenda = db.Column(db.Date, nullable=False) 
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id", ondelete='CASCADE'), nullable=False)
    cliente = db.relationship(Cliente, backref=db.backref("clientes", lazy="dynamic"))
    funcionario_id = db.Column(db.Integer, db.ForeignKey("funcionarios.id", ondelete='CASCADE'), nullable=False)
    funcionario = db.relationship(Funcionario, backref=db.backref("funcionarios", lazy="dynamic"))
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id", ondelete='CASCADE'), nullable=False)
    livro = db.relationship(Livro, backref=db.backref("livros", lazy="dynamic"))
    valor = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return str(self.id)+" - " + self.cliente.nome + " - " + self.livro.titulo