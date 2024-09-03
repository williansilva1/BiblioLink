from App import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from ..entidades import funcionario
from ..services import funcionario_services
from ..forms import cadastro_funcionario_form, editar_funcionario_form
from ..services import funcionario_services

@app.route("/funcionario/", methods=['GET'])
@login_required
def page_funcionario():
    usuarios = funcionario_services.listar_funcionario()
    return render_template("listar_funcionario.html", funcionario=funcionario)

@app.route("/funcionario/cadastrar/", methods=['GET', 'POST'])
@login_required
def page_funcionario_cadastrar():
    form = cadastro_funcionario_form.CadastroFuncionarioForm()
    if form.validate_on_submit():
        funcionario_cadastro = funcionario.Funcionario(
            login = form.login.data,
            senha = form.senha1.data,
            nome = form.nome.data,
            bloqueado = False,
            nivel = 5
        )
        if funcionario_services.cadastrar_funcionario(funcionario_cadastro):
            return redirect(url_for('page_funcionario'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("cadastro_funcionario.html", form=form)


@app.route("/funcionario/mudarstatus/<int:id>/", methods=['POST', 'GET'])
@login_required
def page_funcionario_mudarstatus(id):
    funcionario_services.mudar_status(id)
    return redirect(url_for('page_funcionario'))

@app.route("/funcionario/editar/<int:id>/", methods=['POST', 'GET'])
@login_required
def page_funcionarios_editar(id):
    form = editar_funcionario_form.EditarFuncionarioForm()
    if form.validate_on_submit():
        if funcionario_services.editar_funcionario(id, form.nome.data, form.senha1.data):
            return redirect(url_for('page_funcionarios'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("editar_funcionario.html", form=form, funcionario=funcionario_services.listar_funcionario_id(id))