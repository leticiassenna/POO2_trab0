__author__ = 'Briane'
from abc import ABCMeta, abstractmethod

# Abstract factory class
class DAO_Factory():

    def getDaoAluno(self):
        raise Exception("Preciso ser implementado")

    def getDaoCorda(self):
        raise Exception("Preciso ser implementado")

    def getDaoEndereco(self):
        raise Exception("Preciso ser implementado")

    def getDaoExame(self):
        raise Exception("Preciso ser implementado")

    def getDaoGrupo(self):
        raise Exception("Preciso ser implementado")

