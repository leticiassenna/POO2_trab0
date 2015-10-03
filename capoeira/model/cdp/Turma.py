__author__ = 'Leticia'

class Turma:
    def __int__(self):
        self.nome = ""
        self.turno = ""
        self.horario = ""
        self.dia_semana = ""
        self.rg_aluno = list()
        self.rg_aluno.append(self.rg_aluno[len(self.rg_aluno)])
        self.rg_professor = list()
        self.rg_professor.append(self.rg_professor[len(self.rg_professor)])
        self.cadastro_reserva = list()
        self.cadastro_reserva.append(self.rg_aluno[len(self.cadastro_reserva)])


#o append insere o rg do aluno no final da lista!!