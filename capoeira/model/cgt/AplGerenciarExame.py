__author__ = 'Leticia'

#from capoeira.model.cdp.Exame import Exame
from capoeira.model.cgd.DAOExame import DAOExame
from capoeira.model.cdp.Endereco import Endereco
#from capoeira.model.cdp.Turma import Turma

class AplGerenciarExame(DAOExame):

    def cadastrar(Exame):
        exame = Exame
        exame.hora = Exame.hora
        exame.data = Exame.data
        exame.endereco = Endereco
        exame.endereco = Exame.endereco
        exame.mestre_examinador = Exame.mestre_examinador
        exame.turma = Exame.turma


        daoExame = DAOExame
        daoExame.salvarExame(exame)


    def buscarExame(nome):
        print(nome)

    def excluirExame(dadoExame):
        print(dadoExame)