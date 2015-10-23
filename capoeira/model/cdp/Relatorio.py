__author__ = 'Leticia'

from capoeira.model.cgt.Turma import Turma
from capoeira.model.cgt.Aluno import Aluno


class Relatorio(Turma, Aluno):
    def gerar_relatorio(aluno):

        arquivo = open("relatorio.txt", "r")
        novo_arquivo = arquivo.readlines()
        novo_arquivo.append('\n\n')
        arquivo = open("relatorio.txt", "w")
        arquivo.writelines(novo_arquivo)
        arquivo.write('aluno matriculado: \n\n')
        arquivo.write("Nome: " + aluno.nome)
        arquivo.write('\nRG: ' + aluno.rg)
        arquivo.write('\nData de nascimento: ' + aluno.data_nascimento)
        arquivo.write('\nEndereco: ' + aluno.endereco.logradouro)
        arquivo.write(', ' + aluno.endereco.numero)
        arquivo.write(', ' + aluno.endereco.bairro)
        arquivo.write(', ' + aluno.endereco.cidade)
        arquivo.write(', ' + aluno.endereco.complemento)
        arquivo.write('\nTelefone: ' + aluno.telefone)
        arquivo.write('\nProfissao: ' + aluno.profissao)
        arquivo.write('\nGrau de escolaridade: ' + aluno.grau_escolar)
        arquivo.write('\nNome do pai: ' + aluno.pai)
        arquivo.write('\nNome da mae: ' + aluno.mae)
        arquivo.write('\nCor da corda: ' + aluno.cor_corda)

        arquivo.close()
