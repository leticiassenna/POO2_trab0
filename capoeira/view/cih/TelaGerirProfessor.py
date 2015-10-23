__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cgt.Professor import Professor
from capoeira.model.cgt.Endereco import Endereco

class TelaGerirProfessor (Professor):

    def mensagem(self, msg):
        print(msg)

    def cadastrar_professor(self):
        professor = Professor
        professor.nome = input('Nome do professor: ')
        professor.rg = input('RG professor: ')
        professor.data_nascimento = input('Data de nascimento: ')
        professor.endereco = Endereco()
        professor.endereco = CtrlTelaEndereco.cadastrar_endereco(self)
        professor.telefone = input('Telefone: ')
        professor.profissao = input('Profissao: ')
        professor.grau_escolar = input('Grau de escolaridade: ')
        professor.cor_corda= input('Cor da corda: ')

        print("Professor salvo!")

        return professor


    def buscar_professor(self):
        professor_nome = input('Nome do professor: ')
        return professor_nome


    def excluir_professor(self):
        professor_nome = input('Nome do professor: ')
        return professor_nome
