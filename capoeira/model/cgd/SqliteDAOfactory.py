__author__ = 'Briane'

from capoeira.model.cgd.SqliteDAO import SqliteDAO

class SqliteDAOFactory():

    factory_dao = SqliteDAO()
    def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                 cls._instance = super(SqliteDAOFactory, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def get_dao(self, nome_dao):
        if nome_dao == "Aluno":
           return SqliteDAO().get_dao_aluno(self)
        elif nome_dao == "Corda":
           return SqliteDAO().get_dao_corda(self)
        elif nome_dao == "Exame":
           return SqliteDAO().get_dao_exame(self)
        elif nome_dao == "Turma":
           return SqliteDAO().get_dao_turma(self)
        elif nome_dao == "Professor":
           return SqliteDAO().get_dao_professor(self)
        else:
           return SqliteDAO().get_dao_grupo(self)