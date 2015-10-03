__author__ = 'Leticia'
from capoeira.model.cdp.Pessoa import Pessoa
#from capoeira.model.cdp.Endereco import Endereco


class Aluno(Pessoa):
    def __init__(self):
        super(Pessoa, self).__init__()
        self.pai = ""
        self.mae = ""
        #self.endereco = Endereco


