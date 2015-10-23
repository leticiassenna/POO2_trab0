
__author__ = 'Leticia'
from capoeira.model.cgt.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self):
        super(Pessoa, self).__init__()
        self.pai = ""
        self.mae = ""



