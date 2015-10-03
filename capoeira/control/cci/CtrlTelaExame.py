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

