from flask import render_template, redirect, url_for

from App.livro import blueprint
from App.livro.entidades import Livro
from App.livro.forms import CadastroLivroForm, EditarLivroForm
from App.livro.services import listar_livros, cadastrar_livro, editar_livro, listar_livro_by_id, remover_livro

@blueprint.route("/livros/", methods=['GET'])
def page_livros():
    livros = listar_livros()
    return render_template("livro/listar.html", livros=livros)

@blueprint.route("/livros/cadastrar/", methods=['GET', 'POST'])
def page_livros_cadastrar():
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
            return redirect(url_for('livro_blueprint.page_livros'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")

    return render_template("livro/cadastrar.html", form=form)

@blueprint.route("/livros/alterar/<int:id>/", methods=['GET', 'POST'])
def page_livros_editar(id):
    livro=listar_livro_by_id(id)
    form = EditarLivroForm()
    if form.validate_on_submit():
        livro_editado = Livro(
            titulo=form.titulo.data,
            autor=form.autor.data,
            preco=form.preco.data,
            isbn=livro.isbn,
            estoque=form.estoque.data
        )
        if editar_livro(livro.id, livro_editado):
            return redirect(url_for('livro_blueprint.page_livros', id=id))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")

    return render_template("livro/editar.html", form=form, livro=livro)

@blueprint.route("/livros/<int:id>/", methods=['GET', 'POST'])
def page_livros_consulta(id):
    livro=listar_livro_by_id(id)
    return render_template("livro/consulta.html", livro=livro)

@blueprint.route("/livros/excluir/<int:id>/", methods=['GET',  'POST'])
def page_livros_excluir(id):
    remover_livro(id)    
    return redirect(url_for('livro_blueprint.page_livros'))
    
    
    
