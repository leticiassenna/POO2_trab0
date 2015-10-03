__author__ = 'Leticia'

from capoeira.model.cdp.Aluno import Aluno
from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cdp.Endereco import Endereco

from capoeira.model.cdp.Corda import Corda


class AplGerenciarAluno(DAOAluno):

    def cadastrar(Aluno):
        aluno = Aluno
        aluno.nome = Aluno.nome
        aluno.rg = Aluno.rg
        aluno.data_nascimento = Aluno.data_nascimento
        aluno.endereco = Endereco
        aluno.endereco = Aluno.endereco
        aluno.telefone = Aluno.telefone
        aluno.profissao = Aluno.profissao
        aluno.grau_escolar = Aluno.grau_escolar
        aluno.pai = Aluno.pai
        aluno.mae = Aluno.mae
        aluno.cor_corda = Corda
        aluno.cor_corda = Aluno.cor_corda

        daoAluno = DAOAluno
        daoAluno.salvarAluno(aluno)



    def verificarAluno(self, rg_aluno):
        if rg_aluno ==0000:
            print('cadastrado')
        print('nao cadastrado')
