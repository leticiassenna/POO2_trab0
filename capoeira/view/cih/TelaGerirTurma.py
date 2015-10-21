__author__ = 'Leticia'

from capoeira.model.cdp.Turma import Turma

class TelaGerirTurma (Turma):

    def mensagem(self, msg):
        print(msg)


    def cadastrarTurma(self):
        turma = Turma
        turma.nome = input('Nome da turma: ')
        turma.turno = input('Turno: ')
        turma.horario = input('Horario: ')
        turma.dia_semana = input('Dia da semana: ')
        turma.rg_aluno = []

        while len(turma.rg_aluno)<=20:
            aluno = input("RG do aluno: ")
            turma.rg_aluno.append(aluno)
        while len(turma.rg_aluno)>20:
            print('Cadastro de reserva!!')
            aluno = input("RG do aluno: ")
            cadastro_reserva = []
            turma.cadastro_reserva = cadastro_reserva.append(aluno)
        #print("Aluno cadastrado na turma com sucesso.")
        #self.rg_aluno = input('RG dos alunos: ')

        turma.rg_professor = input('RG do professor: ')

        #turma = []
        #turma.append((self.nome, self.turno, self.horario, self.dia_semana, self.rg_aluno, self.rg_professor))

        print("Turma salvo!")

        return turma



    def buscarTurma(self):
        turmaNome = input('Nome da turma: ')
        return turmaNome


    def excluirTurma(self):
        turmaNome = input('Nome da turma: ')
        return turmaNome