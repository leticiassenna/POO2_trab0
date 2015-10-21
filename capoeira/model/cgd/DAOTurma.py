from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.DAOGeneric import DAOGeneric

__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma


class DAOTuma(Turma):
    def salvar(self, turma):
        dao = DAOGeneric()
        dao.execute_insert_delete("""
        INSERT INTO turma (grau , turno, horario, dia_semana, rg_aluno, rg_professor, cadastro_reserva)
        VALUES (%r,%r,%r,%r,%r,%r,%r,%r)
        """ % (turma.nome, turma.turno, turma.horario, turma.dia_semana, turma.rg_aluno, turma.rg_professor,
               turma.cadastro_reserva))
