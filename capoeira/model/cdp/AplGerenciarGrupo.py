__author__ = 'Leticia'


from capoeira.model.cgd.DAOGrupo import DAOGrupo
from capoeira.model.cgt.Endereco import Endereco
from capoeira.model.cgd.SqliteDAOfactory import SqliteDAOFactory

class AplGerenciarGrupo(DAOGrupo):

    def cadastrar(self, grupo):
        grupo_novo = grupo
        grupo_novo.nome = grupo.nome
        grupo_novo.endereco = Endereco
        grupo_novo.endreco = grupo.endereco
        grupo_novo.sequencia_corda = []
        grupo_novo.sequencia_corda = grupo.sequencia_corda
        dao_grupo = SqliteDAOFactory().get_dao(self, "Grupo")
        dao_grupo.salvar(grupo_novo)


    def buscar_grupo(nome):
        print(nome)

    def excluir_grupo(dado_grupo):
        print(dado_grupo)

