from .pessoa import Usuario

class Cliente():
    def __init__(self, nome, cpf, endereco, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__email = email
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email