__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cdp.Grupo import Grupo
from capoeira.model.cdp.Endereco import Endereco

class TelaGerirGrupo (CtrlTelaEndereco, Grupo):

    def mensagem(self, msg):
        print(msg)

    def cadastrarGrupo(self):
        grupo = Grupo
        grupo.nome = input('Nome do aluno: ')
        grupo.endereco = Endereco
        grupo.endereco = CtrlTelaEndereco.cadastrarEndereco(self)
        #grupo.endereco = input('Endereco: ')
        grupo.sequencia_corda = input('Sequencia das cordas: ')

        #grupo = []
        #grupo.append((self.nome, self.endereco, self.sequencia_corda))

        print("Grupo salvo!")

        return grupo



