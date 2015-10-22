__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cdp.Professor import Professor
from capoeira.model.cdp.Endereco import Endereco
from capoeira.model.cdp.Corda import Corda

class TelaGerirProfessor (Professor):

    def mensagem(self, msg):
        print(msg)

    def cadastrarProfessor(self):
        professor = Professor
        professor.nome = input('Nome do professor: ')
        professor.rg = input('RG professor: ')
        professor.data_nascimento = input('Data de nascimento: ')
        professor.endereco = Endereco()
        professor.endereco = CtrlTelaEndereco.cadastrarEndereco(self)
        #self.endereco = input('Endereco: ')
        professor.telefone = input('Telefone: ')
        professor.profissao = input('Profissao: ')
        professor.grau_escolar = input('Grau de escolaridade: ')
        professor.cor_corda= input('Cor da corda: ')

        #professor = []
        #professor.append((self.nome, self.rg, self.data_nascimento, self.endereco, self.telefone, self.profissao,self.grau_escolaridade, self.cor_corda))

        print("Professor salvo!")

        return professor


    def buscarProfessor(self):
        professorNome = input('Nome do professor: ')
        return professorNome


    def excluirProfessor(self):
        professorNome = input('Nome do professor: ')
        return professorNome
