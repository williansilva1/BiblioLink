from ..models import cliente_model
from App import db

def cadastrar_cliente(cliente):
    cliente_bd = cliente_model(
        nome=cliente.nome,
        cpf=cliente.cpf,
        telefone=cliente.telefone,
        email=cliente.email,
        endereco=cliente.endereco
    )
    db.session.add(cliente_bd)
    db.session.commit()
    return True

def buscar_cliente_cpf(cpf):
    cliente_bd = cliente_model.query.filter_by(cpf=cpf).first()
    return cliente_bd

def editar_funcionario(cpf, cliente):
    cliente_bd = buscar_cliente_cpf(cpf)
    cliente_bd.nome = cliente.nome
    cliente_bd.telefone = cliente.telefone
    cliente_bd.email=cliente.email
    cliente_bd.endereco=cliente.endereco
    db.session.commit()
    return True
def remover_cliente(cpf):
    cliente_bd = buscar_cliente_cpf(cpf)
    db.session.delete(cliente_bd)
    db.session.commit()
    