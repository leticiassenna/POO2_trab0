from capoeira.model.cgd.DAOGeneric import DAOGeneric

__author__ = 'Leticia'

from capoeira.model.cdp.Grupo import Grupo

class DAOGrupo(Grupo):

    def salvar(self, grupo):
        dao = DAOGeneric()
        self.id_endereco = dao.execute_insert_delete("""
        INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
        VALUES (%r,%r,%r,%r,%r)
        """ % (grupo.endereco.logradouro, grupo.endereco.numero, grupo.endereco.bairro, grupo.endereco.cidade, grupo.endereco.complemento))
        dao.execute_insert_delete("""
        INSERT INTO grupo (nome, sequencia_cor , id_endereco)
        VALUES (%r,%r,%r)
        """ % (grupo.nome, grupo.sequencia_corda, self.id_endereco))

