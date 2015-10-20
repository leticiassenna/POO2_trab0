__author__ = 'Leticia'

from capoeira.control.cci.CtrlTelaAluno import CtrlTelaAluno
from capoeira.control.cci.CtrlTelaProfessor import CtrlTelaProfessor
from capoeira.control.cci.CtrlTelaExame import CtrlTelaExame
from capoeira.control.cci.CtrlTelaGrupo import CtrlTelaGrupo
from capoeira.control.cci.CtrlTelaTurma import CtrlTelaTurma


def TelaGerirMenu(self):

    while True:
        print('1- Cadastrar Aluno\n'
              '2- Editar Aluno\n'
              '3- Excluir Aluno\n'
              '4- Cadastrar Professor\n'
              '5- Editar Professor\n'
              '6- Excluir Professor\n'
              '7- Cadastrar Turma\n'
              '8- Editar Turma\n'
              '9- Excluir Turma\n'
              '10- Cadastrar Grupo\n'
              '11- Editar Grupo\n'
              '12- Excluir Grupo\n'
              '13- Cadastrar Exame\n'
              '14- Editar Exame\n'
              '15- Excluir Exame\n'
              '0- Sair\n')

        resposta = int(input('Selecione uma opcao: '))
        if resposta == 1:
            aluno = CtrlTelaAluno
            aluno.cadastrarAluno(self)
        if resposta == 2:
            aluno = CtrlTelaAluno
            aluno.alterarAluno(self)
        if resposta == 3:
            aluno = CtrlTelaAluno
            aluno.excluirAluno(self)
        if resposta == 4:
            professor = CtrlTelaProfessor
            professor.cadastrarProfessor(self)
        if resposta == 5:
            professor = CtrlTelaProfessor
            professor.buscarProfessor(self)
        if resposta == 6:
            professor = CtrlTelaProfessor
            professor.excluirProfessor(self)
        if resposta == 7:
            turma = CtrlTelaTurma
            turma.cadastrarTurma(self)
        if resposta == 8:
            turma = CtrlTelaTurma
            turma.buscarTurma(self)
        if resposta == 9:
            turma = CtrlTelaTurma
            turma.excluirTurma(self)
        if resposta == 10:
            grupo = CtrlTelaGrupo
            grupo.cadastrarGrupo(self)
        if resposta == 11:
            grupo = CtrlTelaGrupo
            grupo.buscarGrupo(self)
        if resposta == 12:
            grupo = CtrlTelaGrupo
            grupo.excluirGrupo(self)
        if resposta == 13:
            exame = CtrlTelaExame
            exame.cadastrarExame(self)
        if resposta == 14:
            exame = CtrlTelaExame
            exame.buscarExame(self)
        if resposta == 15:
            exame = CtrlTelaExame
            exame.excluirExame(self)
        if resposta == 0:
            break

        if resposta > 15:
            print('Opcao invalida!! Digite novamente! ')

