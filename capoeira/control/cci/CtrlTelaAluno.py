__author__ = 'Leticia'

from capoeira.model.cdp.AplGerenciarAluno import AplGerenciarAluno
from capoeira.view.cih.TelaGerirAluno import TelaGerirAluno
from capoeira.model.cdp.Relatorio import Relatorio

class CtrlTelaAluno(AplGerenciarAluno, TelaGerirAluno):

    def cadastrar_aluno(self):
        apl_gerenciar_aluno = AplGerenciarAluno
        tela_gerir_aluno = TelaGerirAluno

        dados_aluno = tela_gerir_aluno.cadastrar_aluno(self)
        apl_gerenciar_aluno.cadastrar(self, dados_aluno)

        relatorio = Relatorio
        relatorio.gerar_relatorio(dados_aluno)

        tela_gerir_aluno.mensagem(self, 'Cadastro realizado!')


    def alterar_aluno(self):
        apl_gerenciar_aluno = AplGerenciarAluno
        tela_gerir_aluno = TelaGerirAluno

        dados_aluno = tela_gerir_aluno.buscar_aluno(self)
        apl_gerenciar_aluno.buscar_aluno(dados_aluno)

    def excluir_aluno(self):
        apl_gerenciar_aluno = AplGerenciarAluno
        tela_gerir_aluno = TelaGerirAluno

        dados_aluno = tela_gerir_aluno.excluir_aluno(self)
        apl_gerenciar_aluno.excluir_aluno(dados_aluno)
