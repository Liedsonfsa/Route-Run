import mysql.connector
from pessoa import Pessoa, Motorista


class Cadastro:

    __slots__ = ['_conexao', '_cursor', '_mysql', '_lista_contas']

    def __init__(self):
        self._lista_contas = []
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS clientes(nome text NOT NULL, endereco text NOT NULL, cpf VARCHAR(11) PRIMARY KEY, nascimento date NOT NULL, usuario text NOT NULL, senha text NOT NULL, email text NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS motoristas(nome text NOT NULL, endereco text NOT NULL, cpf VARCHAR(11) PRIMARY KEY, nascimento date NOT NULL, usuario text NOT NULL, senha text NOT NULL, email text NOT NULL, cnh text NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()

    def cadastrar_usuario(self, pessoa):
        existe = self.busca_cpf_cliente(pessoa.cpf)
        
        if (existe == None):
            self._cursor.execute('INSERT INTO clientes(nome,endereco,cpf,nascimento,usuario,senha,email) VALUES(%s,%s,%s,%s,%s,MD5(%s),%s)', (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento.toString("yyyy-MM-dd"), pessoa.usuario, pessoa.senha, pessoa.email))
            self._conexao.commit()
            return True
        else:
            return False

    def cadastrar_motorista(self, pessoa):
        existe = self.busca_cpf_motorista(pessoa.cpf)
        if (existe == None):
            self._cursor.execute('INSERT INTO motoristas(nome,endereco,cpf,nascimento,usuario,senha,email,cnh) VALUES(%s,%s,%s,%s,%s,MD5(%s),%s,%s)', (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento.toString("yyyy-MM-dd"), pessoa.usuario, pessoa.senha, pessoa.email, pessoa.cnh))
            self._conexao.commit()
            return True
        else:
            return False

    def busca_cpf_motorista(self, cpf):
        self._cursor.execute('SELECT * from motoristas WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista

    def busca_cpf_cliente(self, cpf):
        self._cursor.execute('SELECT * from clientes WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            pessoa = Pessoa(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return pessoa

    def busca_cnh(self, cnh):
        self._cursor.execute('SELECT * from motoristas WHERE cnh = %s',(cnh,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista

    def redefinir(self, email, senha):
        conta_user = self.buscar_email_user(email)
        conta_mot = self.buscar_email_mot(email)

        if conta_user is not None:
            self._cursor.execute('UPDATE clientes SET senha = MD5(%s) WHERE email = %s', (senha, email))
        if conta_mot is not None:
            self._cursor.execute('UPDATE motoristas SET senha = MD5(%s) WHERE email = %s', (senha, email))
        self._conexao.commit()
        if conta_user is not None or conta_mot is not None:
            return True
        else:
            return None

    def buscar_email_mot(self, email):
        self._cursor.execute('SELECT * from motoristas WHERE email = %s',(email,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista


    def buscar_email_user(self, email):
        self._cursor.execute('SELECT * from clientes WHERE email = %s',(email,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            pessoa = Pessoa(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return pessoa

