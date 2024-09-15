from flask import render_template, redirect, url_for

from App.livro import blueprint
from App.livro.entidades import Livro
from App.livro.forms import CadastroLivroForm
from App.livro.services import listar_livros, cadastrar_livro

@blueprint.route("/livros/", methods=['GET'])
def page_livros():
    livros = listar_livros
    return render_template("listar_livros.html", livros=livros)

@blueprint.route("/livros/cadastrar/", methods=['GET', 'POST'])
def page_livro_cadastrar():
    form = CadastroLivroForm()
    if form.validate_on_submit():
        livro_cadastrado = Livro(
            titulo=form.titulo.data,
            autor=form.autor.data,
            isbn=form.isbn.data,
            preco=form.preco.data,
            estoque=form.estoque.data
        )
        if cadastrar_livro(livro_cadastrado):
            return redirect(url_for('page_livros'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")

    return render_template("cadastro_livro.html", form=form)