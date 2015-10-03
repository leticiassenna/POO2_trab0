__author__ = 'Leticia'

from capoeira.model.cdp.Corda import Corda
from capoeira.model.cdp.Endereco import Endereco

class Grupo(Corda, Endereco):
    def grupo(self):
        self.sequencia_corda = []
        self.sequencia_corda.append(Corda.sequencia_corda(self.cor_corda))
        self.nome = ""
        self.endereco = Endereco
