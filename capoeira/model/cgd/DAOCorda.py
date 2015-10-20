from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.DAOGeneric import DAOGeneric

__author__ = 'Gustavo'


class DAOCorda(DAO):

    def salvar(self, corda):
        dao = DAOGeneric()
        dao.execute_insert_delete("""
        INSERT INTO corda (cor)
        VALUES (%r)
        """ % (corda.cor))