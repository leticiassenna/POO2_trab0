__author__ = 'Briane'

from capoeira.model.cgd.Sqlite_DAO import Sqlite_DAO

class Sqlite_DAO_Factory():
    factoryDao = Sqlite_DAO()

    def getDao(self, nomeDao):
        if nomeDao == "Aluno":
           return Sqlite_DAO().getDaoAluno()
        elif nomeDao == "Corda":
           return Sqlite_DAO().getDaoCorda()
        elif nomeDao == "Exame":
           return Sqlite_DAO().getDaoExame()
        else:
           return Sqlite_DAO().getDaoGrupo()