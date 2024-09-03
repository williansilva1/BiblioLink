from App import app
from flask import render_template
from flask_login import login_required, current_user

@app.route("/home/", methods=['GET'])
@login_required
def page_inicio():
    if current_user.nivel == 5:
        print('aparece se tiver nivel 5')
    return render_template("home_livros.html")
