from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class CadastroFuncionarioForm(FlaskForm):
    
    #Dados Cadastrais
    nome = StringField(label="Nome",validators=[Length(min=5, max=70), DataRequired()])
    cpf = StringField(label='Cpf', validators=[Length(min=14, max=14), DataRequired()])
    salario = FloatField(label='Salário', validators=[DataRequired()])
    cargo = StringField(label='Cargo', validators=[Length(max=10, min=3),DataRequired()])
    setor = StringField(label='Setor', validators=[DataRequired()])
    login = StringField(label='Usuário', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])    
    submit = SubmitField(label='Cadastrar')
    
class EditarFuncionarioForm(FlaskForm):
    #Dados cadastrais
    nome=StringField(label="Nome", validators=[DataRequired()])
    salario=FloatField(label='Salário', validators=[DataRequired()])
    cargo=StringField(label='Cargo', validators=[Length(max=10, min=3),DataRequired()])
    setor=StringField(label='Setor', validators=[DataRequired()])
    submit = SubmitField(label="Salvar")
    
class LoginFuncionarioForm(FlaskForm):
    login = StringField(label='Usuário', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')