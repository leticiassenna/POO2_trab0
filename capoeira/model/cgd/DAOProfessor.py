from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.Conexao import Conexao
import copy
__author__ = 'Gustavo'


class DAOProfessor(DAO):

    def clone(self):
        return copy.copy(self)

    def salvar(self, professor):

        try:
            dao = Conexao()
            dao.execute_insert_delete("""
            INSERT INTO pessoa (nome, data_nascimento , telefone , profissao , grau_escolaridade , rg , sequencia_cor)
            VALUES (%r,%r,%r,%r,%r,%r,%r)
            """ % (professor.nome, professor.data_nascimento, professor.telefone, professor.profissao, professor.grau_escolar, professor.rg, professor.cor_corda))
            self.id_endereco = dao.execute_insert_delete("""
            INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
            VALUES (%r,%r,%r,%r,%r)
            """ % (professor.endereco.logradouro, professor.endereco.numero, professor.endereco.bairro, professor.endereco.cidade, professor.endereco.complemento))
            dao.execute_insert_delete("""
            INSERT INTO pessoa_endereco  (id_endereco, rg)
            VALUES (%r,%r)
            """ % (self.id_endereco, professor.rg))
        except ValueError:
            raise

