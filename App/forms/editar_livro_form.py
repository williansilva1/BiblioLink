from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import Length, DataRequired



class EditarLivroForm(FlaskForm):
    titulo = StringField(label='Titulo', validators=[Length(min=5, max=40), DataRequired()])
    autor = StringField(label='Autor', validators=[Length(min=2, max=40), DataRequired()])
    preco = FloatField(label='Preço', validators=[DataRequired()])
    estoque = IntegerField(label='Quantidade em estoque', validators=[DataRequired()])
    
    submit = SubmitField(label="Salvar")