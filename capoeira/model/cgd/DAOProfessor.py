from capoeira.model.cgd.DAOGeneric import DAOGeneric

__author__ = 'Gustavo'


from capoeira.model.cdp.Professor import Professor

class DAOProfessor():

    def salvar(self, professor):
        dao = DAOGeneric()
        dao.execute_insert_delete("""
        INSERT INTO pessoa (nome, data_nascimento , telefone , profissao , grau_escolaridade , rg , cor, id_grupo)
        VALUES (%r,%r,%r,%r,%r,%r,%r,%r)
        """ % (professor.nome, professor.data_nascimento, professor.telefone, professor.profissao, professor.grau_escolar, professor.rg, professor.cor_corda, professor.grupo))
        self.id_endereco = dao.execute_insert_delete("""
        INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
        VALUES (%r,%r,%r,%r,%r)
        """ % (professor.endereco.logradouro, professor.endereco.numero, professor.endereco.bairro, professor.endereco.cidade, professor.endereco.complemento))
        dao.execute_insert_delete("""
        INSERT INTO pessoa_endereco  (id_endereco, rg)
        VALUES (%r,%r)
        """ % (self.id_endereco, professor.rg))
