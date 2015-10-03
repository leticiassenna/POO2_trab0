__author__ = 'Leticia'

from capoeira.model.cdp.Endereco import Endereco

class TelaGerirEndereco (Endereco):

    def mensagem(self, msg):
        print(msg)

    def cadastrarEndereco(self):
        endereco = Endereco
        endereco.logradouro = input('Logradouro: ')
        endereco.numero = input('Numero: ')
        endereco.bairro = input('Bairro: ')
        endereco.cidade = input('Cidade: ')
        endereco.complemento = input('Complemento: ')


        #endereco = ()
        #endereco.append((logradouro, numero, bairro, cidade, complemento))

        print("Endereco salvo!")

        return endereco
