__author__ = 'Leticia'

from capoeira.model.cgd.DAOExame import DAOExame
from capoeira.model.cgt.Endereco import Endereco
from capoeira.model.cgd.SqliteDAOfactory import SqliteDAOFactory

class AplGerenciarExame(DAOExame):

    def cadastrar(self, exame):
        exame_novo = exame
        exame_novo.hora = exame.hora
        exame_novo.data = exame.data
        exame_novo.endereco = Endereco
        exame_novo.endereco = exame.endereco
        exame_novo.mestre_examinador = exame.mestre_examinador
        exame_novo.turma = exame.turma

        dao_exame = SqliteDAOFactory.get_dao(self, "Exame")
        dao_exame.salvarExame(exame_novo)


    def buscar_exame(nome):
        print(nome)

    def excluir_exame(dado_exame):
        print(dado_exame)