__author__ = 'Leticia'


from capoeira.model.cdp.Professor import Professor

class DAOProfessor(Professor):

    def salvarProfessor(self):
        print('Professor salvo: %s' %self.nome)
