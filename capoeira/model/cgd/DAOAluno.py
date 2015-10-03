__author__ = 'Leticia'

from capoeira.model.cdp.Aluno import Aluno

class DAOAluno(Aluno):

    def salvarAluno(self):
        print('Aluno salvo: %s' %self.nome)
