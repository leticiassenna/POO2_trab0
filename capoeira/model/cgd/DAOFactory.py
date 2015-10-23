__author__ = 'Briane'
from abc import ABCMeta, abstractmethod

# Abstract factory class
class DAOFactory():


    @abstractmethod
    def get_dao_aluno(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_corda(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_endereco(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_exame(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_grupo(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_professor(self):
        raise Exception("Preciso ser implementado")
    @abstractmethod
    def get_dao_turma(self):
        raise Exception("Preciso ser implementado")