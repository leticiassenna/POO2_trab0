from capoeira.model.cgd.DAO import DAO
import copy
__author__ = 'Leticia'


class DAOExame(DAO):

    def clone(self):
        return copy.copy(self)

    def salvar(self):
        print('Exame salvo: %s, %s' %(self.data,self.hora))

