__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.model.cgt.Aluno import Aluno
from capoeira.model.cgt.Endereco import Endereco

class TelaGerirAluno(CtrlTelaEndereco):

    def mensagem(self, msg):
        print(msg)


    def cadastrar_aluno(self):
        aluno = Aluno
        aluno.nome = input('Nome do aluno: ')
        aluno.rg = input('RG aluno: ')
        aluno.data_nascimento = input('Data de nascimento: ')
        aluno.endereco = Endereco
        aluno.endereco = CtrlTelaEndereco.cadastrar_endereco(self)
        aluno.telefone = input('Telefone: ')
        aluno.profissao = input('Profissao: ')
        aluno.grau_escolar = input('Grau de escolaridade: ')
        aluno.pai = input('Nome do pai: ')
        aluno.mae = input('Nome da mae: ')
        aluno.cor_corda = input('Cor da corda: ')
        aluno.grupo = input('Nome Grupo: ')

        print("Aluno salvo!")

        return aluno


    def buscar_aluno(self):
        aluno_nome = input('Nome do aluno: ')
        return aluno_nome


    def excluir_aluno(self):
        aluno_nome = input('Nome do aluno: ')
        return aluno_nome
