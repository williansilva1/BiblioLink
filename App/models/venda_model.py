from App import db
from models import livro_model, cliente_model, funcionario_model

class Venda(db.Model):
    __tablename__ = "vendas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    dataVenda = db.Column(db.Date, nullable=False) 
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id", ondelete='CASCADE'), nullable=False)
    cliente = db.relationship(cliente_model.Cliente, backref=db.backref("clientexvenda", lazy="dynamic"), overlaps="clientexvenda")
    funcionario_id = db.column(db.Integer, db.ForeingKey("funcionarios.id", ondelete='CASCADE'), nullable=False)
    funcionario = db.relationship(funcionario_model.Funcionario, backref=db.backref("funcionarioxvenda", lazy="dynamic"), overlaps="funcionarioxvenda")
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id", ondelete='CASCADE'), nullable=False)
    livro = db.relationship(livro_model.Livro, backref=db.backref("livrosxvenda", lazy="dynamic"), overlaps="livrosxvenda")
    valor = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return str(self.id)+" - " + self.cliente.nome + " - " + self.livro.titulo