from App import db
from App.venda.models import Venda


def listar_vendas():
    vendas = Venda.query.all()
    return vendas

