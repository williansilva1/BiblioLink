from App import app
from flask import render_template, redirect, url_for
from ..services import livro_services
from ..forms import cadastro_livro_form
from ..entidades import livro

@app.route("/livros/", methods=['GET'])
def page_livros():
    livros = livro_services.listar_livros
    return render_template("listar_livros.html", livros=livros)

@app.route("/livros/cadastrar/", methods=['GET', 'POST'])
def page_livro_cadastrar():
    form = cadastro_livro_form.CadastroLivroForm()
    if form.validate_on_submit():
        livro_cadastrado = livro.Livro(
            titulo=form.titulo.data,
            autor=form.autor.data,
            isbn=form.isbn.data,
            preco=form.preco.data,
            estoque=form.estoque.data
        )
        if livro_services.cadastrar_livro(livro_cadastrado):
            return redirect(url_for('page_livros'))
    if form.errors != {}:
        for field, err in form.errors.items():
            print(f"Error in field {field}: {err}")

    return render_template("cadastro_livro.html", form=form)

    #if form validar
    #monta entidade de livro
    #chama o serviço de cadastro passando entidade
    #se verdadeiro cadastrou, logo faz o que vc quer fazer quando cadastro
    #se falso, deu algum erro no momento de gravar no BD, logo é interessante informar ao usuario o motivo
    
    """
    Orientações template
    
    Substituir imput por {{ form.campo(class="classe do css") }}
    substituir label por {{ form.campo.label(class="classe do css") }}
    
    Exemplo completo
    
    <form method="POST" class="form-register">
                    {{ form.hidden_tag() }}
                    <div class="mdc-text-field">
                      {{ form.descricao(class="mdc-text-field__input") }}
                      <div class="mdc-line-ripple"></div>
                      {{ form.descricao.label(class="mdc-floating-label") }}
                    </div>
                    <div class="mdc-text-field">
                      {{ form.cbo(class="mdc-text-field__input") }}
                      <div class="mdc-line-ripple"></div>
                      {{ form.cbo.label(class="mdc-floating-label") }}
                    </div>
                    <div class="template-demo">
                    {{ form.submit(class="btn btn-primary") }}
                    </div>
                  </form>
    """