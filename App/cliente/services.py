from App import db
from App.cliente.models import Cliente

def cadastrar_cliente(cliente):
    cliente_bd = Cliente(
        nome=cliente.nome,
        cpf=cliente.cpf,
        email=cliente.email,
        endereco=cliente.endereco
    )
    db.session.add(cliente_bd)
    db.session.commit()
    return True

def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.id).all()

def listar_clientes():
    clientes = Cliente.query.all()
    return clientes

def buscar_cliente_cpf(cpf):
    cliente_bd = Cliente.query.filter_by(cpf=cpf).first()
    return cliente_bd

def buscar_cliente_id(id):
    cliente_bd = Cliente.query.filter_by(id=id).first()
    return cliente_bd

def editar_cliente(id, cliente):
    cliente_bd = buscar_cliente_id(id)
    cliente_bd.nome = cliente.nome
    cliente_bd.email=cliente.email
    cliente_bd.endereco=cliente.endereco
    db.session.commit()
    return True

def remover_cliente(id):
    cliente = Cliente.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()
    return True
    