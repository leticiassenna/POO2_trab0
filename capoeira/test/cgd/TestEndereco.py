__author__ = 'Leticia'

import unittest
from capoeira.model.cgt.AplGerenciarEndereco import AplGerenciarEndereco
from capoeira.model.cdp.Endereco import Endereco


class TestEndereco(unittest.TestCase):
    def testEndereco(self):
        """

        :type self: AplGerenciarEndereco
        """
        e = Endereco
        e.logradouro = 'Rua Lumberto Maciel de Azevedo'
        e.numero = '370'
        e.bairro = 'Jardim Camburi'
        e.cidade = 'Vitoria'
        e.complemento = 'Ed. Ilha do Sol'

        aplGerenciarEndereco = AplGerenciarEndereco
        aplGerenciarEndereco.cadastrar(e)

        self.assertEqual(aplGerenciarEndereco.logradouro, e.logradouro)


if __name__ == '__main__':
    unittest.main()
