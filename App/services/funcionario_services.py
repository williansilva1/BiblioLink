from App import db
from ..models import funcionario_model

def cadastrar_funcionario(funcionario):
    funcionario_bd = funcionario_model(
        nome=funcionario.nome,
        cpf=funcionario.cpf,
        salario=funcionario.salario,
        cargo=funcionario.cargo,
        setor=funcionario.setor,
        endereco=funcionario.endereco,
        email=funcionario.email
    )
    db.session.add(funcionario_bd)
    db.session.commit()
    return True

def  buscar_funcionario_cpf(cpf):
    funcionario_bd = funcionario_model.query.filter_by(cpf=cpf).first()
    return funcionario_bd

def editar_funcionario(cpf, funcionario):
    funcionario_db = buscar_funcionario_cpf(cpf)
    funcionario_db.nome=funcionario.nome
    funcionario_db.salario=funcionario.salario
    funcionario_db.cargo=funcionario.cargo
    funcionario_db.setor=funcionario.setor
    funcionario_db.endereco=funcionario.endereco
    funcionario_db.email=funcionario.email
    db.session.commit()
    return True

def remover_funcionario(cpf):
    funcionario_bd = buscar_funcionario_cpf(cpf)
    db.session.delete(funcionario_bd)
    db.session.commit()
    



    