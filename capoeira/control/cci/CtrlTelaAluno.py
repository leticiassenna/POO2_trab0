__author__ = 'Leticia'

from capoeira.model.cgt.AplGerenciarAluno import AplGerenciarAluno
from capoeira.view.cih.TelaGerirAluno import TelaGerirAluno
from capoeira.model.cgt.Relatorio import Relatorio

class CtrlTelaAluno(AplGerenciarAluno, TelaGerirAluno):

    def cadastrarAluno(self):
        aplGerenciarAluno = AplGerenciarAluno
        telaGerirAluno = TelaGerirAluno

        #dadosAluno = []
        dadosAluno = telaGerirAluno.cadastrarAluno(self)
        aplGerenciarAluno.cadastrar(dadosAluno)

        relatorio = Relatorio
        relatorio.gerar_relatorio(aplGerenciarAluno)

        telaGerirAluno.mensagem(self, 'Cadastro realizado!')
