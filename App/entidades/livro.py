class Livro():
    def __init__(self, titulo, autor, isbn, preco, estoque):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__preco = preco
        self.__estoque = estoque
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
        
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco
        
    @property
    def estoque(self):
        return self.__estoque
    
    @estoque.setter
    def estoque(self,estoque):
        self.__estoque = estoque