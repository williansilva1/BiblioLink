from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class vendaForm (FlaskForm):
    cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    livro = StringField('Livro', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=1, message="Quantidade deve ser pelo menos 1")])
    preco = DecimalField('Preço Unitário', validators=[DataRequired(), NumberRange(min=0.01, message="O preço deve ser maior que zero")])
    
    submit = SubmitField('Registrar Venda')