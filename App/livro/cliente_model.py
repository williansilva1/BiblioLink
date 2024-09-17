from App import db

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    #nome, cpf, endereço, email
    nome=db.column(db.String(40), nullable=False )
    cpf=db.column(db.String(14), unique=True, nullable=False)
    endereco=db.column(db.String(30), nullable=False)
    email=db.column(db.String(30), nullable=False)
    
    def __repr__(self):
        return str(self.id) + " - " + self.nome