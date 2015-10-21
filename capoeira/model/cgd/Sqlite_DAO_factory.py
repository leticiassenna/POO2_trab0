__author__ = 'Briane'

from capoeira.model.cgd.Sqlite_DAO import Sqlite_DAO

class Sqlite_DAO_Factory():
    factoryDao = Sqlite_DAO

    def getDao(self, nomeDao):
        if nomeDao == "Aluno":
           return Sqlite_DAO.getDaoAluno(self)
        elif nomeDao == "Corda":
           return Sqlite_DAO.getDaoCorda(self)
        elif nomeDao == "Exame":
           return Sqlite_DAO.getDaoExame(self)
        else:
           return Sqlite_DAO.getDaoGrupo(self)