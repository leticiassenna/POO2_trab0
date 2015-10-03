__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma
from capoeira.model.cdp.Endereco import Endereco

class Exame(Turma):
    def __init__(self):
        self.hora = ""
        self.data = ""
        self.endereco = Endereco
        self.mestre_examinador = ""
        self.turma = Turma



