from App import db
from App.funcionario.models import Funcionario

def cadastrar_funcionario(funcionario):
    funcionario_bd = Funcionario(
        nome=funcionario.nome,
        cpf=funcionario.cpf,
        salario=funcionario.salario,
        cargo=funcionario.cargo,
        setor=funcionario.setor,
        endereco=funcionario.endereco,
        email=funcionario.email,
        login=funcionario.login,
        senha=funcionario.senha
    )
    db.session.add(funcionario_bd)
    db.session.commit()
    return True

def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return funcionarios

def buscar_funcionario_cpf(cpf):
    funcionario_bd = Funcionario.query.filter_by(cpf=cpf).first()
    return funcionario_bd

def buscar_funcionario_login(login):
    funcionario_bd=Funcionario.query.filter_by(login=login).first
    return funcionario_bd

def buscar_funcionario_id(id):
    funcionario_bd = Funcionario.query.filter_by(id=id).first()
    return funcionario_bd
    
def editar_funcionario(cpf, funcionario):
    funcionario_db = buscar_funcionario_cpf(cpf)
    funcionario_db.nome=funcionario.nome
    funcionario_db.salario=funcionario.salario
    funcionario_db.cargo=funcionario.cargo
    funcionario_db.setor=funcionario.setor
    funcionario_db.endereco=funcionario.endereco
    funcionario_db.email=funcionario.email
    funcionario_db.login=funcionario.login
    funcionario_db.senha=funcionario.senha
    db.session.commit()
    return True

def remover_funcionario(cpf):
    funcionario_bd = buscar_funcionario_cpf(cpf)
    db.session.delete(funcionario_bd)
    db.session.commit()
    



    