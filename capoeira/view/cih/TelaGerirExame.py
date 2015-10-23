__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cgt.Exame import Exame
from capoeira.model.cgt.Endereco import Endereco

class TelaGerirExame (CtrlTelaEndereco, Exame):

    def mensagem(self, msg):
        print(msg)

    def cadastrar_exame(self):
        exame = Exame
        exame.hora = input('Hora: ')
        exame.data = input('Data: ')
        exame.endereco = Endereco
        exame.endereco = CtrlTelaEndereco.cadastrar_endereco(self)
        exame.mestre_examinador = input('Mestre Examinador: ')
        exame.turma = input('Turma a ser avaliada: ')

        print("Exame salvo!")

        return exame


    def buscar_exame(self):
        dados = input('Dia do exame: ')
        return dados


    def excluir_exame(self):
        dados = input('Dia do exame: ')
        return dados