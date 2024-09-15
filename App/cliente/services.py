from App import db
from App.cliente.models import Cliente

def cadastrar_cliente(cliente):
    cliente_bd = Cliente(
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
    cliente = Cliente.query.filter_by(cpf=cpf).first()
    return cliente

def buscar_cliente_id(id):
    cliente = Cliente.query.filter_by(id=id).first()

def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.id).all()

def editar_cliente(cpf, cliente):
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
    