from App import app
from ..forms import venda_form
from flask import render_template, redirect, url_for


@app.route("/venda/", methods=['GET', 'POST'])
def page_venda():
    form = venda_form.vendaForm()
        

    return render_template("venda.html", form=form)
