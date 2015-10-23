from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.Conexao import Conexao
import copy
__author__ = 'Leticia'


class DAOGrupo(DAO):
    def clone(self):
            return copy.copy(self)

    def salvar(self, grupo):
        try:
            dao = Conexao()
            id_endereco = dao.execute_insert_delete("""
            INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
            VALUES (%r,%r,%r,%r,%r)
            """ % (grupo.endereco.logradouro, grupo.endereco.numero, grupo.endereco.bairro, grupo.endereco.cidade,
                   grupo.endereco.complemento))

        except ValueError:
            raise
