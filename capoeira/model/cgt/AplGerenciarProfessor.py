__author__ = 'Leticia'

from capoeira.model.cdp.Corda import Corda
from capoeira.model.cgd.DAOProfessor import DAOProfessor
from capoeira.model.cdp.Endereco import Endereco


class AplGerenciarProfessor(DAOProfessor, Corda):
    def cadastrar(Professor):
        professor = Professor
        professor.nome = Professor.nome
        professor.rg = Professor.rg
        professor.data_nascimento = Professor.data_nascimento
        professor.endereco = Endereco
        professor.endereco = Professor.endereco
        professor.telefone = Professor.telefone
        professor.profissao = Professor.profissao
        professor.grau_escolar = Professor.grau_escolar
        professor.cor_corda = Professor.cor_corda

        daoProfessor = DAOProfessor()
        daoProfessor.salvar(professor)



    def buscarProfessor(nome):
        print(nome)

    def excluirProfessor(dadoProfessor):
        print(dadoProfessor)

