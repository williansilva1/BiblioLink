from App import db
from App.livro.models import Livro

def cadastrar_livro(livro):
    livro_bd = Livro(
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
    return Livro.query.filter_by(id=id).first()

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
    livro = Livro.query.filter_by(id=id).first()
    db.session.delete(livro)
    db.session.commit()
    return True

def listar_livros():
    return Livro.query.order_by(Livro.id).all()

def listar_livros_estoque():
    livros = Livro.query.filter(Livro.estoque>0).order_by(Livro.id).all()
    return livros


    #livros = Livro.query.order_by(Livro.id).all()
    #livros_estoque=[]
    #for livro in livros:
    #    print(livro.estoque)
    #    if (livro.estoque > 0):
    #        print(livro.titulo)
    #        livros_estoque.append(livro)
    #return livros_estoque
    
