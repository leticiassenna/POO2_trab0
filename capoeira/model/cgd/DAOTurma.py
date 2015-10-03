__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma

class DAOTuma(Turma):

    def salvarTurma(self):
        print('Turma salvo: %s' %self.nome)
