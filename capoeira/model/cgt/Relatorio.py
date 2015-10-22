__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma
from capoeira.model.cdp.Aluno import Aluno


class Relatorio(Turma, Aluno):
    def gerar_relatorio(Aluno):

        arquivo = open("relatorio.txt", "r")
        novoArquivo = arquivo.readlines()
        novoArquivo.append('\n\n')
        arquivo = open("relatorio.txt", "w")
        arquivo.writelines(novoArquivo)
        arquivo.write('Aluno matriculado: \n\n')
        arquivo.write("Nome: " + Aluno.nome)
        arquivo.write('\nRG: ' + Aluno.rg)
        arquivo.write('\nData de nascimento: ' + Aluno.data_nascimento)
        arquivo.write('\nEndereco: ' + Aluno.endereco.logradouro)
        arquivo.write(', ' + Aluno.endereco.numero)
        arquivo.write(', ' + Aluno.endereco.bairro)
        arquivo.write(', ' + Aluno.endereco.cidade)
        arquivo.write(', ' + Aluno.endereco.complemento)
        arquivo.write('\nTelefone: ' + Aluno.telefone)
        arquivo.write('\nProfissao: ' + Aluno.profissao)
        arquivo.write('\nGrau de escolaridade: ' + Aluno.grau_escolar)
        arquivo.write('\nNome do pai: ' + Aluno.pai)
        arquivo.write('\nNome da mae: ' + Aluno.mae)
        arquivo.write('\nCor da corda: ' + Aluno.cor_corda)
        # for linha in arquivo.readlines():
        #    print(linha)

        arquivo.close()
