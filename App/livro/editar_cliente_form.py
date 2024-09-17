from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import Length, DataRequired

#alterar livro > cliente

class EditarClienteForm(FlaskForm):
    nome = StringField(label='Nome', validators=[Length(min=5, max=40), DataRequired()])
    endereco=StringField(label='Endereco', validators=[DataRequired()])
    email=StringField(label='Email', validators=[DataRequired()])
   
    
    submit = SubmitField(label="Salvar")