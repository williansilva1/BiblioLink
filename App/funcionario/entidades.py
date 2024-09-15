class Funcionario():
    def __init__(self, nome, cpf, salario, cargo, setor, login, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__cargo = cargo
        self.__setor = setor
        self.__login = login
        self.__senha = senha
        
    
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
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
        
    @property
    def cargo(self):
        return self.__cargo
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
    
    @property
    def setor(self):
        return self.__setor
    @setor.setter
    def setor(self, setor):
        self.__setor = setor
        
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, login):
        self.__login = login
        
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha