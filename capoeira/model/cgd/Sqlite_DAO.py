from capoeira.model.cgd.DAOProfessor import DAOProfessor

__author__ = 'Briane'
from capoeira.model.cgd.DAO_Factory import DAO_Factory
from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cgd.DAOCorda import DAOCorda
from capoeira.model.cgd.DAOExame import DAOExame
from capoeira.model.cgd.DAOGrupo import DAOGrupo
from capoeira.model.cgd.DAOTurma import DAOTurma
from capoeira.model.cgd import DAO


class Sqlite_DAO(DAO_Factory):

    __salvar_aluno = DAOAluno()
    __salvar_corda = DAOCorda()
    __salvar_exame = DAOExame()
    __salvar_grupo = DAOGrupo()
    __salvar_professor = DAOProfessor()
    __salvar_turma = DAOTurma()

    def getDaoAluno(self):
        return Sqlite_DAO().__salvar_aluno.clone()

    def getDaoCorda(self):
        return Sqlite_DAO().__salvar_corda.clone()


    def getDaoExame(self):
        return Sqlite_DAO().__salvar_exame.clone()

    def getDaoGrupo(self):
        return Sqlite_DAO().__salvar_grupo.clone()

    def getDaoProfessor(self):
        return Sqlite_DAO().__salvar_professor.clone()

    def getDaoTurma(self):
        return Sqlite_DAO().__salvar_turma.clone()

