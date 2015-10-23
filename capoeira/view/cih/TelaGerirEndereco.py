__author__ = 'Leticia'

from capoeira.model.cgt.Endereco import Endereco

class TelaGerirEndereco(Endereco):

    def mensagem(self, msg):
        print(msg)

    def cadastrar_endereco(self):
        endereco = Endereco
        endereco.logradouro = input('Logradouro: ')
        endereco.numero = input('Numero: ')
        endereco.bairro = input('Bairro: ')
        endereco.cidade = input('Cidade: ')
        endereco.complemento = input('Complemento: ')

        print("Endereco salvo!")

        return endereco
