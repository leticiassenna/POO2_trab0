__author__ = 'Briane'
from capoeira.model.cgd.DAO_Factory import DAO_Factory
from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cgd.DAOCorda import DAOCorda
from capoeira.model.cgd.DAOExame import DAOExame
from capoeira.model.cgd.DAOGrupo import DAOGrupo
from capoeira.model.cgd import DAO


class Sqlite_DAO(DAO_Factory):
    def getDaoAluno(self):
        return DAOAluno()

    def getDaoCorda(self):
        return DAOCorda()

    def getDaoExame(self):
        return DAOExame()

    def getDaoGrupo(self):
        return DAOGrupo()
