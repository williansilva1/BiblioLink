from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DecimalField, DateField
from wtforms.validators import DataRequired, NumberRange


class vendaForm (FlaskForm):
    dataVenda = DateField('Data da venda', validators=[DataRequired()])
    cliente = SelectField('Nome do Cliente', choices=[], validators=[DataRequired()])
    preco = DecimalField('Preço', validators=[DataRequired()])
    
    submit = SubmitField('Registrar Venda')