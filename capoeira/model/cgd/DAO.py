from abc import abstractmethod

__author__ = 'Gustavo'


class DAO():

    @abstractmethod
    def gravar_banco(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def deletar(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def listar(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def clone(self):
        raise Exception("Preciso ser implementado")