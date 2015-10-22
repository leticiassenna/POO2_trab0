from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.DAOGeneric import DAOGeneric
import copy
__author__ = 'Leticia'

from capoeira.model.cdp.Grupo import Grupo

class DAOGrupo(DAO):
    def clone(self):
            return copy.copy(self)

    def salvar(self, grupo):
        try:
            dao = DAOGeneric()
            id_endereco = dao.execute_insert_delete("""
            INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
            VALUES (%r,%r,%r,%r,%r)
            """ % (grupo.endereco.logradouro, grupo.endereco.numero, grupo.endereco.bairro, grupo.endereco.cidade, grupo.endereco.complemento))
            #dao.execute_insert_delete("""
            #INSERT INTO grupo (nome, cor, id_endereco)
            #VALUES (%r,%r,%r)
            #""" % (grupo.nome, grupo.sequencia_corda, id_endereco))
        except ValueError:
            raise
