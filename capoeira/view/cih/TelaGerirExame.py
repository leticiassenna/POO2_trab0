__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cdp.Exame import Exame
from capoeira.model.cdp.Endereco import Endereco
#from capoeira.model.cdp.Turma import Turma

class TelaGerirExame (CtrlTelaEndereco, Exame):

    def mensagem(self, msg):
        print(msg)

    def cadastrarExame(self):
        exame = Exame
        exame.hora = input('Hora: ')
        exame.data = input('Data: ')
        exame.endereco = Endereco
        exame.endereco = CtrlTelaEndereco.cadastrarEndereco(self)
        #self.endereco = input('Endereco: ')
        exame.mestre_examinador = input('Mestre Examinador: ')
        #exame.turma = Turma
        exame.turma = input('Turma a ser avaliada: ')

        #exame = []
        #exame.append((self.hora, self.data, self.endereco, self.meste_examinador, self.turma))

        print("Exame salvo!")

        return exame

