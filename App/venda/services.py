from App import db
from App.venda.models import Venda


def listar_vendas():
    vendas = Venda.query.all()
    return vendas


def cadastrar_venda(venda):
    venda_bd = Venda(
        data=venda.data,
        cliente_id=venda.cliente.id,
        funcionario_id=venda.funcionario.id,
        livro_id=venda.livro.id,
        valor=venda.valor
    )
    db.session.add(venda_bd)
    db.session.commit()
    return True
    
