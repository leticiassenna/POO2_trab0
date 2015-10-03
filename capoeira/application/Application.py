__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaAluno import CtrlTelaAluno
from capoeira.control.cci.CtrlTelaProfessor import CtrlTelaProfessor
from capoeira.control.cci.CtrlTelaEndereco import CtrlTelaEndereco
from capoeira.control.cci.CtrlTelaExame import CtrlTelaExame
from capoeira.control.cci.CtrlTelaGrupo import CtrlTelaGrupo
from capoeira.control.cci.CtrlTelaTurma import CtrlTelaTurma
from capoeira.model.cdp.Aluno import Aluno


# class Application:
def main(self):

    while True:
        print('1- Cadastrar Aluno\n'
              '2- Cadastrar Professor\n'
              '3- Cadastrar Turma\n'
              '4- Cadastrar Grupo\n'
              '5- Cadastrar Exame\n'
              '0- Sair\n')

        resposta = int(input('Selecione uma opcao: '))
        if resposta == 1:
            aluno = CtrlTelaAluno
            aluno.cadastrarAluno(self)
        if resposta == 2:
            professor = CtrlTelaProfessor
            professor.cadastrarProfessor(self)
        if resposta == 3:
            turma = CtrlTelaTurma
            turma.cadastrarTurma(self)
        if resposta == 4:
            grupo = CtrlTelaGrupo
            grupo.cadastrarGrupo(self)
        if resposta == 5:
            exame = CtrlTelaExame
            exame.cadastrarExame(self)
        if resposta == 0:
            break

        if resposta > 5:
        #    print('\n1- Cadastrar Aluno\n'
        #          '2- Cadastrar Professor\n'
        #          '3- Cadastrar Turma\n'
        #          '4- Cadastrar Grupo\n'
        #          '5- Cadastrar Exame\n')
            print('Opcao invalida!! Digite novamente! ')



if __name__ == "__main__":
    main(self="")
