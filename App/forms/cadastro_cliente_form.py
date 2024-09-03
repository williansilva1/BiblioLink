from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length


class CadastroClienteForm(FlaskForm):
    #Dados Cadastrais
    nome=StringField(label="Nome", validators=[DataRequired()])
    cpf=StringField(label='Cpf', validators=[DataRequired()])
    endereco=StringField(label='Endereco', validators=[DataRequired()])
    email=StringField(label='Email', validators=[DataRequired()])
    login = StringField(label='Usuário', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')