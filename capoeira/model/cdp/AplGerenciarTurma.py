from capoeira.model.cgd.SqliteDAOfactory import SqliteDAOFactory

__author__ = 'Leticia'

from capoeira.model.cgd.DAOTurma import DAOTurma

class AplGerenciarTurma(DAOTurma):

    def cadastrar(self, turma):
        turma_nova = turma
        turma_nova.nome = turma.nome
        turma_nova.turno = turma.turno
        turma_nova.horario = turma.horario
        turma_nova.rg_aluno = turma.rg_aluno
        turma_nova.rg_professor = turma.rg_professor
        turma_nova.cadastro_reserva = turma.cadastro_reserva

        dao_turma = SqliteDAOFactory().get_dao(self, "Turma")
        dao_turma.salvarTurma(turma_nova)


    def buscar_turma(nome):
        print(nome)

    def excluir_turma(dado_turma):
        print(dado_turma)