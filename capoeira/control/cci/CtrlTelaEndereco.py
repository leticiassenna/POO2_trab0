__author__ = 'Leticia'


from capoeira.model.cdp.AplGerenciarEndereco import AplGerenciarEndereco
from capoeira.view.cih.TelaGerirEndereco import TelaGerirEndereco


class CtrlTelaEndereco(AplGerenciarEndereco, TelaGerirEndereco):

    def cadastrar_endereco(self):
        apl_gerenciar_endereco = AplGerenciarEndereco
        tela_gerir_endereco = TelaGerirEndereco

        dados_endereco = tela_gerir_endereco.cadastrar_endereco(self)
        apl_gerenciar_endereco.cadastrar(self, dados_endereco)

        tela_gerir_endereco.mensagem(self, 'Cadastro realizado!')
