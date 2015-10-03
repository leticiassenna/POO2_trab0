__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cdp.Aluno import Aluno
from capoeira.model.cdp.Endereco import Endereco
from capoeira.model.cdp.Corda import Corda

class TelaGerirAluno(CtrlTelaEndereco):

    def mensagem(self, msg):
        print(msg)

    def cadastrarAluno(self):
        aluno = Aluno
        aluno.nome = input('Nome do aluno: ')
        aluno.rg = input('RG aluno: ')
        aluno.data_nascimento = input('Data de nascimento: ')
        aluno.endereco = Endereco
        aluno.endereco = CtrlTelaEndereco.cadastrarEndereco(self)
        #self.endereco = input('Endereco: ')
        aluno.telefone = input('Telefone: ')
        aluno.profissao = input('Profissao: ')
        aluno.grau_escolar = input('Grau de escolaridade: ')
        aluno.pai = input('Nome do pai: ')
        aluno.mae = input('Nome da mae: ')
        aluno.cor_corda = Corda
        aluno.cor_corda.cor = input('Cor da corda: ')

        #aluno = []
       # aluno.append((nome, rg, data_nascimento, endereco, telefone, profissao,grau_escolaridade, pai, mae))

        print("Aluno salvo!")

        return aluno


