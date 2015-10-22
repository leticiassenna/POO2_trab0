from capoeira.model.cgd.DAO import DAO
import copy
__author__ = 'Leticia'


from capoeira.model.cdp.Exame import Exame

class DAOExame(DAO):

    def clone(self):
        return copy.copy(self)

    def salvar(self):
        print('Exame salvo: %s, %s' %(self.data,self.hora))

