from capoeira.model.cgd.Sqlite_DAO_factory import Sqlite_DAO_Factory

__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma
from capoeira.model.cgd.DAOTurma import DAOTurma

class AplGerenciarTurma(DAOTurma):

    def cadastrar(Turma):
        turma = Turma
        turma.nome = Turma.nome
        turma.turno = Turma.turno
        turma.horario = Turma.horario
        turma.rg_aluno = Turma.rg_aluno
        turma.rg_professor = Turma.rg_professor
        turma.cadastro_reserva = Turma.cadastro_reserva

        daoTurma = Sqlite_DAO_Factory().getDao( "Turma")
        daoTurma.salvarTurma(turma)


    def buscarTurma(nome):
        print(nome)

    def excluirTurma(dadoTurma):
        print(dadoTurma)