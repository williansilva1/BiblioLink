from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user

from App import app
from App.funcionario import blueprint
from App.funcionario.entidades import Funcionario
from App.funcionario.forms import CadastroFuncionarioForm,EditarFuncionarioForm, LoginFuncionarioForm
from App.funcionario.services import buscar_funcionario_cpf, cadastrar_funcionario, editar_funcionario, remover_funcionario, buscar_funcionario_id, buscar_funcionario_login, listar_funcionarios

#Autenticacao
@blueprint.route('/')
def route_default():
    return redirect(url_for('funcionario_blueprint.login'))

# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginFuncionarioForm(request.form)
    if 'login' in request.form:

        # read form data
        login = request.form['login']
        senha = request.form['senha']

        # Locate user
        funcionario =  buscar_funcionario_login(login)

        # Check the password
        if funcionario and funcionario.validar_senha(senha):
            login_user(funcionario)
            return redirect(url_for('funcionario_blueprint.route_default'))
        

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('funcionario_blueprint.login'))

@blueprint.route("/funcionario/", methods=['GET'])
def page_funcionario():
    funcionarios = listar_funcionarios()
    return render_template("funcionario/listar.html", funcionarios=funcionarios)

@blueprint.route("/funcionario/cadastrar/", methods=['GET', 'POST'])
#@login_required
def page_funcionario_cadastrar():
    form = CadastroFuncionarioForm()
    if form.validate_on_submit():
        funcionario_cadastro = Funcionario(
            login = form.login.data,
            senha = form.senha1.data,
            nome = form.nome.data,
            bloqueado = False,
            nivel = 5
        )
        if cadastrar_funcionario(funcionario_cadastro):
            return redirect(url_for('funcionario_blueprint.page_funcionario_cadastrar'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("funcionario/cadastrar.html", form=form)


@blueprint.route("/funcionario/editar/<int:id>/", methods=['POST', 'GET'])
#@login_required
def page_funcionarios_editar(id):
    form = EditarFuncionarioForm()
    funcionario = buscar_funcionario_id(id)
    if form.validate_on_submit():
        if editar_funcionario(id, form.nome.data, form.senha1.data):
            return redirect(url_for('page_funcionarios'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")
            flash(f"Erro ao atualizar cadastro {field}: {err}", category='danger')

    return render_template("funcionario/editar.html", form=form, funcionario=funcionario)