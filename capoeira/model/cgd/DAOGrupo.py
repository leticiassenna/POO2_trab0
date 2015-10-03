__author__ = 'Leticia'

from capoeira.model.cdp.Grupo import Grupo

class DAOGrupo(Grupo):

    def salvarGrupo(self):
        print('Grupo salvo: %s' %self.nome)
