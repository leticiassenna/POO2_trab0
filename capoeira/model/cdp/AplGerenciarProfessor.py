from capoeira.model.cgd.SqliteDAOfactory import SqliteDAOFactory

__author__ = 'Leticia'

from capoeira.model.cgt.Corda import Corda
from capoeira.model.cgd.DAOProfessor import DAOProfessor
from capoeira.model.cgt.Endereco import Endereco


class AplGerenciarProfessor(DAOProfessor, Corda):

    def cadastrar(self, professor):
        professor_novo = professor
        professor_novo.nome = professor.nome
        professor_novo.rg = professor.rg
        professor_novo.data_nascimento = professor.data_nascimento
        professor_novo.endereco = Endereco
        professor_novo.endereco = professor.endereco
        professor_novo.telefone = professor.telefone
        professor_novo.profissao = professor.profissao
        professor_novo.grau_escolar = professor.grau_escolar
        professor_novo.cor_corda = professor.cor_corda

        dao_professor = SqliteDAOFactory().get_dao(self, "Professor")
        dao_professor.salvar(professor_novo)



    def buscar_professor(nome):
        print(nome)

    def excluir_professor(dado_professor):
        print(dado_professor)

