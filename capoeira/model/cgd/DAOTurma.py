from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.DAOGeneric import DAOGeneric
import copy
__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma


class DAOTuma(DAO):

    def clone(self):
            return copy.copy(self)

    def salvar(self, turma):
        try:
            dao = DAOGeneric()
            dao.execute_insert_delete("""
            INSERT INTO turma (grau , turno, rg_professor )
            VALUES (%r,%r,%r,%r,%r,%r,%r,%r)
            """ % (turma.nome, turma.dia_semana, turma.rg_professor))
        except ValueError:
            raise

