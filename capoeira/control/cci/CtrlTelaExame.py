__author__ = 'Leticia'

from capoeira.model.cgt.AplGerenciarExame import AplGerenciarExame
from capoeira.view.cih.TelaGerirExame import TelaGerirExame


class CtrlTelaExame(AplGerenciarExame, TelaGerirExame):

    def cadastrarExame(self):
        aplGerenciarExame = AplGerenciarExame
        telaGerirExame = TelaGerirExame

        #dadosExame = []
        dadosExame = telaGerirExame.cadastrarExame(self)
        aplGerenciarExame.cadastrar(dadosExame)

        telaGerirExame.mensagem(self, 'Cadastro realizado!')



    def alterarExame(self):
        aplGerenciarExame = AplGerenciarExame
        telaGerirExame = TelaGerirExame

        dadosExame = telaGerirExame.buscarExame(self)
        aplGerenciarExame.buscarExame(dadosExame)

    def excluirExame(self):
        aplGerenciarExame = AplGerenciarExame
        telaGerirExame = TelaGerirExame

        dadosExame = telaGerirExame.excluirExame(self)
        aplGerenciarExame.excluirExame(dadosExame)