from capoeira.model.cgd.DAOProfessor import DAOProfessor

__author__ = 'Briane'
from capoeira.model.cgd.DAOFactory import DAOFactory
from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cgd.DAOCorda import DAOCorda
from capoeira.model.cgd.DAOExame import DAOExame
from capoeira.model.cgd.DAOGrupo import DAOGrupo
from capoeira.model.cgd.DAOTurma import DAOTurma


class SqliteDAO(DAOFactory):

    def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                 cls._instance = super(SqliteDAO, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    __salvar_aluno = DAOAluno()
    __salvar_corda = DAOCorda()
    __salvar_exame = DAOExame()
    __salvar_grupo = DAOGrupo()
    __salvar_professor = DAOProfessor()
    __salvar_turma = DAOTurma()

    def get_dao_aluno(self):
        return SqliteDAO().__salvar_aluno.clone(self)

    def get_dao_corda(self):
        return SqliteDAO().__salvar_corda.clone(self)

    def get_dao_exame(self):
        return SqliteDAO().__salvar_exame.clone(self)

    def get_dao_grupo(self):
        return SqliteDAO().__salvar_grupo.clone(self)

    def get_dao_professor(self):
        return SqliteDAO().__salvar_professor.clone(self)

    def get_dao_turma(self):
        return SqliteDAO().__salvar_turma.clone(self)

