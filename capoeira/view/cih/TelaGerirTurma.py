__author__ = 'Leticia'

from capoeira.model.cgt.Turma import Turma

class TelaGerirTurma (Turma):

    def mensagem(self, msg):
        print(msg)


    def cadastrar_turma(self):
        turma = Turma
        turma.nome = input('Nome da turma: ')
        turma.turno = input('Turno: ')
        turma.horario = input('Horario: ')
        turma.dia_semana = input('Dia da semana: ')
        turma.rg_aluno = []
        cadastro_reserva=[]

        while len(turma.rg_aluno)<=20:
            aluno = input("RG do aluno: ")
            turma.rg_aluno.append(aluno)
        while len(cadastro_reserva)<5:
            print('Cadastro de reserva!!')
            aluno = input("RG do aluno: ")
            turma.cadastro_reserva = cadastro_reserva.append(aluno)

        turma.rg_professor = input('RG do professor: ')

        print("Turma salvo!")

        return turma



    def buscar_turma(self):
        turma_nome = input('Nome da turma: ')
        return turma_nome


    def excluir_turma(self):
        turma_nome = input('Nome da turma: ')
        return turma_nome
