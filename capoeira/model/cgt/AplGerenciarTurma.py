__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma
from capoeira.model.cgd.DAOTurma import DAOTuma

class AplGerenciarTurma(DAOTuma):

    def cadastrar(Turma):
        turma = Turma
        turma.nome = Turma.nome
        turma.turno = Turma.turno
        turma.horario = Turma.horario
        turma.rg_aluno = Turma.rg_aluno
        turma.rg_professor = Turma.rg_professor
        turma.cadastro_reserva = Turma.cadastro_reserva

        daoTurma = DAOTuma
        daoTurma.salvarTurma(turma)
