__author__ = 'Leticia'


from capoeira.model.cgt.AplGerenciarEndereco import AplGerenciarEndereco
from capoeira.view.cih.TelaGerirEndereco import TelaGerirEndereco


class CtrlTelaEndereco(AplGerenciarEndereco, TelaGerirEndereco):

    def cadastrarEndereco(self):
        aplGerenciarEndereco = AplGerenciarEndereco
        telaGerirEndereco = TelaGerirEndereco

        #dadosEndereco = []
        dadosEndereco = telaGerirEndereco.cadastrarEndereco(self)
        aplGerenciarEndereco.cadastrar(dadosEndereco)

        telaGerirEndereco.mensagem(self, 'Cadastro realizado!')
