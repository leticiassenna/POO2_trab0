__author__ = 'Leticia'

from capoeira.model.cgd.DAOGeneric import DAOGeneric
from capoeira.model.cdp.Endereco import Endereco


def salvar(self, endereco):
        dao = DAOGeneric()

        dao.execute_insert_delete("""
        INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
        VALUES (%r,%r,%r,%r,%r)
        """ % (endereco.logradouro, endereco.numero, endereco.bairro, endereco.cidade,
               endereco.complemento))

