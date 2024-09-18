from App.venda import blueprint
from App import app
from App.venda.forms import vendaForm
from App.venda.entidades import Venda
from App.venda.services import listar_vendas, cadastrar_venda
from App.livro.services import listar_livros_estoque, listar_livro_by_id
from App.cliente.services import listar_clientes
from App.funcionario.services import buscar_funcionario_id
from flask import render_template, redirect, url_for
from flask_login import current_user
from datetime import date


@blueprint.route("/venda/cadastrar/", methods=['GET', 'POST'])
def page_venda_cadastrar():
    form = vendaForm()
    return render_template("venda.html", form=form)

@blueprint.route("/venda/", methods=['GET'])
def page_venda():
    vendas = listar_vendas()
    return render_template("venda/listar.html", vendas=vendas)

def page_vender_livro(id):
    form = vendaForm()
    livro = listar_livro_by_id(id)
    funcionario = buscar_funcionario_id(current_user.id)
    clientes = listar_clientes()
    for cliente in clientes:
        form.cliente.choices.append(cliente)
    if form.validate_on_submit():
        venda = Venda(
            valor = form.preco.data,
            dataVenda = form.dataVenda.data,
            cliente = form.cliente.data,
            funcionario=funcionario,
            livro=livro
            )
        if cadastrar_venda(venda):
            return redirect(url_for('funcionario_blueprint.page_funcionario'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")

    return render_template("funcionario/cadastrar.html", form=form)