__author__ = 'Leticia'

import unittest
from capoeira.model.cdp.AplGerenciarEndereco import AplGerenciarEndereco
from capoeira.model.cgt.Endereco import Endereco


class TestEndereco(unittest.TestCase):
    def test_endereco(self):
        e = Endereco
        e.logradouro = 'Rua Lumberto Maciel de Azevedo'
        e.numero = '370'
        e.bairro = 'Jardim Camburi'
        e.cidade = 'Vitoria'
        e.complemento = 'Ed. Ilha do Sol'

        apl_gerenciar_endereco = AplGerenciarEndereco
        apl_gerenciar_endereco.cadastrar(e)

        self.assertEqual(apl_gerenciar_endereco.logradouro, e.logradouro)


if __name__ == '__main__':
    unittest.main()
