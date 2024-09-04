from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import Length, DataRequired



class EditarFuncionarioForm(FlaskForm):
    #Dados cadastrais
    nome=StringField(label="Nome", validators=[DataRequired()])
    salario=FloatField(label='Salário', validators=[DataRequired()])
    cargo=StringField(label='Cargo', validators=[Length(max=10, min=3),DataRequired()])
    setor=StringField(label='Setor', validators=[DataRequired()])
    
    submit = SubmitField(label="Salvar")
    
    
    