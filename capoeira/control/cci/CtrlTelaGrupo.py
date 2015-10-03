__author__ = 'Leticia'

from capoeira.model.cgt.AplGerenciarGrupo import AplGerenciarGrupo
from capoeira.view.cih.TelaGerirGrupo import TelaGerirGrupo


class CtrlTelaGrupo(AplGerenciarGrupo, TelaGerirGrupo):

    def cadastrarGrupo(self):
        aplGerenciarGrupo = AplGerenciarGrupo
        telaGerirGrupo = TelaGerirGrupo

       # dadosGrupo = []
        dadosGrupo = telaGerirGrupo.cadastrarGrupo(self)
        aplGerenciarGrupo.cadastrar(dadosGrupo)

        telaGerirGrupo.mensagem(self, 'Cadastro realizado!')
