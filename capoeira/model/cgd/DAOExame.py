__author__ = 'Leticia'


from capoeira.model.cdp.Exame import Exame

class DAOExame(Exame):

    def salvarExame(self):
        print('Exame salvo: %s, %s' %(self.data,self.hora))

