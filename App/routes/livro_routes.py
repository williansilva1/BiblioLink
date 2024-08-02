from App import app
from flask import render_template
from ..services import livro_services
from ..forms import cadastro_livro_form

@app.route("/livros/", methods=['GET'])
def page_livros():
    livros = livro_services.listar_livros
    return render_template("listar_livros.html", livros = livros)

@app.route("/livros/cadastrar/", methods=['GET', 'POST'])
def page_livro_cadastrar():
    form = cadastro_livro_form.CadastroLivroForm()
    return render_template("cadastrar_livro.html", form=form)