__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cgt.Grupo import Grupo
from capoeira.model.cgt.Endereco import Endereco

class TelaGerirGrupo (CtrlTelaEndereco, Grupo):

    def mensagem(self, msg):
        print(msg)

    def cadastrar_grupo(self):
        grupo = Grupo()
        grupo.nome = input('Nome do aluno: ')
        grupo.endereco = Endereco
        grupo.endereco = CtrlTelaEndereco.cadastrar_endereco(self)
        grupo.sequencia_corda = input('Sequencia das cordas: ')

        print("Grupo salvo!")

        return grupo



    def buscar_grupo(self):
        grupo_nome = input('Nome do grupo: ')
        return grupo_nome


    def excluir_grupo(self):
        grupo_nome = input('Nome do grupo: ')
        return grupo_nome
