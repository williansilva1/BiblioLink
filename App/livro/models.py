from App import db

class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(40), nullable=False)
    autor = db.Column(db.String(40), nullable=False)
    isbn = db.Column(db.String(14), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
       
    def __repr__(self):
        return str(self.id) + " - " + self.titulo