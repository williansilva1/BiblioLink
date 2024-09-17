from App import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from ..entidades import cliente
from ..services import cliente_services
from ..forms import cadastro_cliente_form, editar_cliente_form

@app.route("/cliente/", methods=['GET'])
@login_required
def page_cliente():
    usuarios = cliente_services.listar_cliente()
    return render_template("listar_cliente.html", cliente=cliente)

@app.route("/cliente/cadastrar/", methods=['GET', 'POST'])
@login_required
def page_cliente_cadastrar():
    form = cadastro_cliente_form.CadastroClienteForm()
    if form.validate_on_submit():
        cliente_cadastro = cliente.Cliente(
            login = form.login.data,
            senha = form.senha1.data,
            nome = form.nome.data,
            bloqueado = False,
            nivel = 5
        )
        if cliente_services.cadastrar_cliente(cliente_cadastro):
            return redirect(url_for('page_cliente'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("cadastro_cliente.html", form=form)


@app.route("/cliente/mudarstatus/<int:id>/", methods=['POST', 'GET'])
@login_required
def page_cliente_mudarstatus(id):
    cliente_services.mudar_status(id)
    return redirect(url_for('page_cliente'))

@app.route("/cliente/editar/<int:id>/", methods=['POST', 'GET'])
@login_required
def page_clientes_editar(id):
    form = editar_cliente_form.EditarClienteForm()
    if form.validate_on_submit():
        if cliente_services.editar_cliente(id, form.nome.data, form.senha1.data):
            return redirect(url_for('page_clientes'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("editar_cliente.html", form=form, cliente=cliente_services.listar_cliente_id(id))