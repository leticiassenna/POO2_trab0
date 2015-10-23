__author__ = 'Leticia'

from capoeira.model.cdp.AplGerenciarProfessor import AplGerenciarProfessor
from capoeira.view.cih.TelaGerirProfessor import TelaGerirProfessor


class CtrlTelaProfessor(AplGerenciarProfessor, TelaGerirProfessor):

    def cadastrar_professor(self):
        apl_gerenciar_professor = AplGerenciarProfessor
        tela_gerir_professor = TelaGerirProfessor

        dados_professor = tela_gerir_professor.cadastrar_professor(self)
        apl_gerenciar_professor.cadastrar(self, dados_professor)

        tela_gerir_professor.mensagem(self, 'Cadastro realizado!')


    def alterar_professor(self):
        apl_gerenciar_professor = AplGerenciarProfessor
        tela_gerir_professor = TelaGerirProfessor

        dados_professor = tela_gerir_professor.buscar_professor(self)
        apl_gerenciar_professor.buscar_professor(dados_professor)

    def excluir_professor(self):
        apl_gerenciar_professor = AplGerenciarProfessor
        tela_gerir_professor = TelaGerirProfessor

        dados_professor = tela_gerir_professor.excluir_professor(self)
        apl_gerenciar_professor.excluir_professor(dados_professor)