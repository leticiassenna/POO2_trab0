__author__ = 'Leticia'

from capoeira.model.cdp.AplGerenciarTurma import AplGerenciarTurma
from capoeira.view.cih.TelaGerirTurma import TelaGerirTurma


class CtrlTelaTurma(AplGerenciarTurma, TelaGerirTurma):

    def cadastrar_aluno(self):
        apl_gerenciar_turma = AplGerenciarTurma
        tela_gerir_turma = TelaGerirTurma

        dados_turma = tela_gerir_turma.cadastrar_turma(self)
        apl_gerenciar_turma.cadastrar(self, dados_turma)

        tela_gerir_turma.mensagem(self,'Cadastro realizado!')


    def alterar_turma(self):
        apl_gerenciar_turma = AplGerenciarTurma
        tela_gerir_turma = TelaGerirTurma

        dados_turma = tela_gerir_turma.buscar_turma(self)
        apl_gerenciar_turma.buscar_turma(dados_turma)

    def excluir_turma(self):
        apl_gerenciar_turma = AplGerenciarTurma
        tela_gerir_turma = TelaGerirTurma

        dados_turma = tela_gerir_turma.excluir_turma(self)
        apl_gerenciar_turma.excluir_turma(dados_turma)