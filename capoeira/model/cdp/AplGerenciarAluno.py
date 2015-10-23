__author__ = 'Leticia'


from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cgt.Endereco import Endereco
from capoeira.model.cgd.SqliteDAOfactory import SqliteDAOFactory


class AplGerenciarAluno(DAOAluno):

    def cadastrar(self, aluno):
        aluno_novo = aluno
        aluno_novo.nome = aluno.nome
        aluno_novo.rg = aluno.rg
        aluno_novo.data_nascimento = aluno.data_nascimento
        aluno_novo.endereco = Endereco
        aluno_novo.endereco = aluno.endereco
        aluno_novo.telefone = aluno.telefone
        aluno_novo.profissao = aluno.profissao
        aluno_novo.grau_escolar = aluno.grau_escolar
        aluno_novo.pai = aluno.pai
        aluno_novo.mae = aluno.mae
        aluno_novo.cor_corda = aluno.cor_corda
        aluno_novo.grupo = aluno.grupo

        dao_aluno = SqliteDAOFactory().get_dao(self, "Aluno")

        dao_aluno.salvar(aluno_novo)



    def verificar_aluno(self, rg_aluno):
        if rg_aluno ==0000:
            print('cadastrado')
        print('nao cadastrado')


    def buscar_aluno(nome):
        print(nome)

    def excluir_aluno(dado_aluno):
        print(dado_aluno)
