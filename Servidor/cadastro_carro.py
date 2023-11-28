import abc
import mysql.connector


class Carro(abc.ABC):

    __slots__ = ['_placa', '_tipo', '_modelo', '_cpf']

    def __init__(self, placa, tipo, modelo, cpf):
        self._placa = placa
        self._tipo = tipo
        self._modelo = modelo
        self._cpf = cpf

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf


class CadCarro:

    __slots__ = ['_conexao', '_cursor', '_mysql']

    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS carros(placa VARCHAR(11) PRIMARY KEY, tipo text NOT NULL, modelo text NOT NULL, cpf VARCHAR(11), foreign key(cpf) references motoristas(cpf));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_carro(self, carro):
        existe = self.busca_carro(carro.placa)
        if (existe == None):
            self._cursor.execute('INSERT INTO carros(placa, tipo, modelo, cpf) VALUES(%s,%s,%s,%s)', (carro.placa, carro.tipo, carro.modelo, carro.cpf))
            self._conexao.commit()
            return True
        else:
            return False

    def busca_carro(self, placa):
        self._cursor.execute('SELECT * from carros WHERE placa = %s',(placa,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            carro = Carro(verificar[0], verificar[1], verificar[2], verificar[3])
            return carro
