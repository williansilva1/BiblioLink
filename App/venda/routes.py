from App.venda import blueprint
from App import app
from App.venda.forms import vendaForm
from App.venda.services import listar_vendas
from flask import render_template, redirect, url_for


@blueprint.route("/venda/cadastrar/", methods=['GET', 'POST'])
def page_venda_cadastrar():
    form = vendaForm()
    return render_template("venda.html", form=form)

@blueprint.route("/venda/", methods=['GET'])
def page_venda():
    vendas = listar_vendas
    return render_template("venda.html", vendas=vendas)