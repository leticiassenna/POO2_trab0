__author__ = 'Leticia'

from capoeira.model.cdp.Endereco import Endereco
from capoeira.model.cgd.DAOEndereco import DAOEndereco

class AplGerenciarEndereco(DAOEndereco):

    def cadastrar(Endereco):
        endereco = Endereco
        endereco.logradouro = Endereco.logradouro
        endereco.numero = Endereco.numero
        endereco.bairro = Endereco.bairro
        endereco.cidade = Endereco.cidade
        endereco.complemento = Endereco.complemento

        daoEndereco = DAOEndereco
        daoEndereco.salvarEndereco(endereco)


