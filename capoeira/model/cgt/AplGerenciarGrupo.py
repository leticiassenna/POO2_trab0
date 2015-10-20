__author__ = 'Leticia'

from capoeira.model.cdp.Grupo import Grupo
from capoeira.model.cgd.DAOGrupo import DAOGrupo
from capoeira.model.cdp.Endereco import Endereco

class AplGerenciarGrupo(DAOGrupo):

    def cadastrar(Grupo):
        grupo = Grupo
        grupo.nome = Grupo.nome
        grupo.endereco = Endereco
        grupo.endreco = Grupo.endereco
        grupo.sequencia_corda = []
        grupo.sequencia_corda = Grupo.sequencia_corda


        daoGrupo = DAOGrupo
        daoGrupo.salvarGrupo(grupo)


    def buscarGrupo(nome):
        print(nome)

    def excluirAlunoGrupo(dadoGrupo):
        print(dadoGrupo)