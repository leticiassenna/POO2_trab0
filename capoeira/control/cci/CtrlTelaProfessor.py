__author__ = 'Leticia'

from capoeira.model.cgt.AplGerenciarProfessor import AplGerenciarProfessor
from capoeira.view.cih.TelaGerirProfessor import TelaGerirProfessor


class CtrlTelaProfessor(AplGerenciarProfessor, TelaGerirProfessor):

    def cadastrarProfessor(self):
        aplGerenciarProfessor = AplGerenciarProfessor
        telaGerirProfessor = TelaGerirProfessor

        #dadosProfessor = []
        dadosProfessor = telaGerirProfessor.cadastrarProfessor(self)
        aplGerenciarProfessor.cadastrar(dadosProfessor)

        telaGerirProfessor.mensagem(self, 'Cadastro realizado!')
