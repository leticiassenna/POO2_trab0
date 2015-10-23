__author__ = 'Leticia'

from capoeira.model.cdp.AplGerenciarGrupo import AplGerenciarGrupo
from capoeira.view.cih.TelaGerirGrupo import TelaGerirGrupo


class CtrlTelaGrupo(AplGerenciarGrupo, TelaGerirGrupo):

    def cadastrar_grupo(self):
        apl_gerenciar_grupo = AplGerenciarGrupo
        tela_gerir_grupo = TelaGerirGrupo

        dados_grupo = tela_gerir_grupo.cadastrar_grupo(self)
        apl_gerenciar_grupo.cadastrar(self, dados_grupo)

        tela_gerir_grupo.mensagem(self, 'Cadastro realizado!')


    def alterar_grupo(self):
        apl_gerenciar_grupo = AplGerenciarGrupo
        tela_gerir_grupo = TelaGerirGrupo

        dados_grupo = tela_gerir_grupo.buscar_grupo(self)
        apl_gerenciar_grupo.buscar_grupo(dados_grupo)

    def excluir_grupo(self):
        apl_gerenciar_grupo = AplGerenciarGrupo
        tela_gerir_grupo = TelaGerirGrupo

        dados_grupo = tela_gerir_grupo.excluir_grupo(self)
        apl_gerenciar_grupo.excluir_grupo(dados_grupo)