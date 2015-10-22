__author__ = 'Gustavo'
import sqlite3
class DAOGeneric():
    def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                 cls._instance = super(DAOGeneric, cls).__new__(cls, *args, **kwargs)
            return cls._instance
    def __init__(self):


        self.conn = sqlite3.connect("po2.db")


        self.cursor = self.conn.cursor()

        # cria uma tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS corda (
        cor text PRIMARY KEY
        )""")
        self.conn.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  endereco (
        logadouro text,
        numero text,
        bairro text,
        cidade text,
        complemento text,
        id_endereco INTEGER PRIMARY KEY autoincrement
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS grupo (
        id_grupo INTEGER PRIMARY KEY autoincrement,
        nome text,
        cor text,
        id_endereco INTEGER,
        FOREIGN KEY(cor) REFERENCES corda (cor),
        FOREIGN KEY(id_endereco) REFERENCES endereco (id_endereco)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa (nome text, data_nascimento text, telefone text, profissao text, grau_escolaridade text, rg text PRIMARY KEY unique, sequencia_cor text,id_grupo text)""")

        self.conn.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS turma (grau text, turno text, id_turma INTEGER PRIMARY KEY autoincrement,rg_professor text, FOREIGN KEY(rg_professor) REFERENCES pessoa (rg))""")
        self.conn.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS horarioSemana (
        dia text,
        horario text,
        id_horario INTEGER PRIMARY KEY autoincrement
        )""")
        self.conn.commit()


        self.cursor.execute("""CREATE TABLE IF NOT EXISTS horario_turma (
        id_horario INTEGER,
        id_turma INTEGER,
        FOREIGN KEY(id_horario) REFERENCES horarioSemana (id_horario),
        FOREIGN KEY(id_turma) REFERENCES turma (id_turma)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa_grupo (
        rg text,
        nome text,
        FOREIGN KEY(rg) REFERENCES pessoa (rg),
        FOREIGN KEY(nome) REFERENCES grupo (nome)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS filiacao (
        nome_pai text,
        nome_mae text,
        rg text,
        FOREIGN KEY(rg) REFERENCES pessoa (rg)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa_endereco (
        id_endereco INTEGER,
        rg text,
        FOREIGN KEY(rg) REFERENCES pessoa (rg),
        FOREIGN KEY(id_endereco) REFERENCES endereco (id_endereco)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  estuda (
        rg text,
        id_turma INTEGER,
        FOREIGN KEY(rg) REFERENCES pessoa (rg),
        FOREIGN KEY(id_turma) REFERENCES turma (id_turma)
        )""")
        self.conn.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS exame (
        data DATETIME,
        hora DATETIME,
        id_endereco INTEGER,
        rg text,
        FOREIGN KEY(rg) REFERENCES pessoa (rg),
        FOREIGN KEY(id_endereco) REFERENCES endereco (id_endereco)
        )""")
        self.conn.commit()
        self.conn.close()

#metodo que conecta ao banco de dados
    def connect_db(self):
        try:
            # conectando...

            self.conn = sqlite3.connect("po2.db")

            self.cursor = self.conn.cursor()
        except sqlite3.Error:
            print("Erro ao abrir banco.")
# metodo para exeutar operacoes sem retorno ao banco de dados
    def execute_insert_delete(self, modificador):

        try:
            self.connect_db()
            self.cursor.execute(modificador)
            self.close_db()
            return self.cursor.lastrowid
        except:
            raise

#metodo para selecionar algo do banco de dados
    def execute_select(self, string_para_selecao):
        self.connect_db()
        self.cursor.execute(string_para_selecao)
        lista_pessoas = self.cursor.fetchall()
        self.close_db()
        return lista_pessoas

# metodo que executa e finaliza o banco de dados
    def close_db(self):
         self.commit_db()
         if self.conn:
             self.conn.close()


    def commit_db(self):
        if self.conn:
            self.conn.commit()

