from App import app
from flask import render_template, flash, redirect, url_for
from ..forms import login_form
#from ..services import usuario_services
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/", methods=['GET', 'POST'])
def page_home():
    if current_user.is_authenticated:
        return redirect(url_for('page_inicio'))
    else:
        return redirect(url_for('page_login'))


@app.route("/login/", methods=['GET', 'POST'])
def page_login():
    if current_user.is_authenticated:
        return redirect(url_for('page_inicio'))
    form = login_form.LoginUsuarioForm()
    if form.validate_on_submit():
        usuario_logado = usuario_services.listar_usuario_login(login=form.login.data)
        if usuario_logado and usuario_logado.validar_senha(form.senha.data):
            login_user(usuario_logado)
            flash(f'Bem vindo, {usuario_logado.login}!', category='success')
            return redirect(url_for('page_inicio'))
        else:
            flash(f'Usuário ou senha estão incorretos! Tente novamente.', category='danger')

    return render_template("login.html", form=form)

@app.route("/logout")
def page_logout():
    logout_user()
    flash("Você finalizou seu acesso.", category="info")
    return redirect(url_for("page_login"))