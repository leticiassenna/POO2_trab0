
__author__ = 'Leticia'

from capoeira.model.cgt.Endereco import Endereco


class Pessoa:

    def __init__(self):
        self.nome = ""
        self.rg = ""
        self.data_nascimento = ""
        self.endereco = Endereco
        self.telefone = ""
        self.profissao = ""
        self.grau_escolar = ""
        self.cor_corda = ""
        self.grupo = ''

        self.endereco = Endereco()