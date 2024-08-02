from ..models import livro_model
from App import db

def cadastrar_livro(livro):
    livro_bd = livro_model.Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        isbn = livro.isbn,
        preco = livro.preco,
        estoque = livro.estoque
    )
    db.session.add(livro_bd)
    db.session.commit()
    return True

def listar_livro_by_id(id):
    return livro_model.Livro.query.filter_by(id).first()

def editar_livro(id, livro):
    livro_db = listar_livro_by_id(id)
    livro_db.titulo = livro.titulo 
    livro_db.autor = livro.autor
    livro_db.isbn = livro.isbn
    livro_db.preco = livro.preco
    livro_db.estoque = livro.estoque
    db.session.commit()
    return True

def remover_livro(id):
    db.session.delete(listar_livro_by_id(id))
    return True

def listar_livros():
    return livro_model.Livro.query.order_by(livro_model.Livro.id).all()