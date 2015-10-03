__author__ = 'Leticia'

from capoeira.model.cdp.Endereco import Endereco

class DAOEndereco(Endereco):

    def salvarEndereco(self):
        print('Endereco salvo: %s' %self.logradouro)
