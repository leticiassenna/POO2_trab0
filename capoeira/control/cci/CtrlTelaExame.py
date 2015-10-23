__author__ = 'Leticia'

from capoeira.model.cdp.AplGerenciarExame import AplGerenciarExame
from capoeira.view.cih.TelaGerirExame import TelaGerirExame


class CtrlTelaExame(AplGerenciarExame, TelaGerirExame):

    def cadastrar_exame(self):
        apl_gerenciar_exame = AplGerenciarExame
        tela_gerir_exame = TelaGerirExame

        dados_exame = tela_gerir_exame.cadastrar_exame(self)
        apl_gerenciar_exame.cadastrar(self, dados_exame)

        tela_gerir_exame.mensagem(self, 'Cadastro realizado!')



    def alterar_exame(self):
        apl_gerenciar_exame = AplGerenciarExame
        tela_gerir_exame = TelaGerirExame

        dados_exame = tela_gerir_exame.buscar_exame(self)
        apl_gerenciar_exame.buscar_exame(self, dados_exame)

    def excluir_exame(self):
        apl_gerenciar_exame = AplGerenciarExame
        tela_gerir_exame = TelaGerirExame

        dados_exame = tela_gerir_exame.excluir_exame(self)
        apl_gerenciar_exame.excluir_exame(self, dados_exame)