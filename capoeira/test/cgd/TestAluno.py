from capoeira.model.cgt.Corda import Corda
from capoeira.model.cgt.Endereco import Endereco
from capoeira.model.cgd.DAOAluno import DAOAluno
from capoeira.model.cgd.DAOCorda import DAOCorda

__author__ = 'Leticia'

import unittest
from capoeira.model.cgt.Aluno import Aluno
from capoeira.model.cdp.AplGerenciarAluno import AplGerenciarAluno


class TestAuno(unittest.TestCase):

    def test_aluno(self):
        dao = DAOAluno()
        a = Aluno()
        corda = Corda()
        a.nome = 'Leticia'
        a.rg = '337654jikh3'
        a.data_nascimento = '04/11/1991'
        a.profissao = 'Estudante'
        a.grau_escolar = 'Superior incompleto'
        a.endereco = Endereco
        a.endereco.logradouro = 'Rua Lumberto Maciel de Azevedo'
        a.endereco.numero = '370'
        a.endereco.bairro = 'Jardim Camburi'
        a.endereco.cidade = 'Vitoria'
        a.endereco.complemento = 'Ed. Ilha do Sol'
        a.telefone = '30848471'
        a.pai = 'Leonardo'
        a.mae = 'Deise'
        a.cor_corda = 'Violetblue'
        corda.cor = 'Vlyfest'
        DAOCorda().salvar(corda)
        a.grupo = ''

        apl_gerenciar_aluno = AplGerenciarAluno()
        apl_gerenciar_aluno.cadastrar(a)
        #self.assertEqual(apl_gerenciar_aluno.nome, a.nome)



if __name__ == '__main__':
    unittest.main()
