from App import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from App.cliente import blueprint
from App.cliente.entidades import Cliente
from App.cliente.forms import CadastroClienteForm, EditarClienteForm
from App.cliente.services import cadastrar_cliente, listar_clientes, editar_cliente, buscar_cliente_id, remover_cliente

@blueprint.route("/cliente/", methods=['GET'])
#@login_required
def page_cliente():
    clientes = listar_clientes()
    return render_template("cliente/listar.html", clientes=clientes)

@blueprint.route("/cliente/cadastrar/", methods=['GET', 'POST'])
#@login_required
def page_cliente_cadastrar():
    form = CadastroClienteForm()
    if form.validate_on_submit():
        cliente_cadastro = Cliente(
            nome = form.nome.data,
            cpf=  form.cpf.data,
            endereco = form.endereco.data,
            email = form.email.data
        )
        if cadastrar_cliente(cliente_cadastro):
            return redirect(url_for('cliente_blueprint.page_cliente_cadastrar'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("cliente/cadastrar.html", form=form)

@blueprint.route("/cliente/editar/<int:id>/", methods=['POST', 'GET'])
#@login_required
def page_clientes_editar(id):
    form = EditarClienteForm()
    cliente = buscar_cliente_id(id)
    if form.validate_on_submit():
        cliente_editado = Cliente( 
                nome=form.nome.data,
                cpf=cliente.cpf,
                endereco=form.endereco.data,
                email=form.email.data
        )
        if editar_cliente(id, cliente_editado):
            return redirect(url_for('cliente_blueprint.page_cliente'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("cliente/editar.html", form=form, cliente=buscar_cliente_id(id))

@blueprint.route("/cliente/<int:id>/", methods=['GET', 'POST'])
#@login_required
def page_clientes_consultar(id):
    cliente=buscar_cliente_id(id)
    return render_template("cliente/consultar.html", cliente=cliente)

@blueprint.route("/cliente/excluir/<int:id>/", methods=['GET',  'POST'])
#@login_required
def page_clientes_excluir(id):
    remover_cliente(id)    
    return redirect(url_for('cliente_blueprint.page_cliente'))