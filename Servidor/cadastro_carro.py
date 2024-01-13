import abc
import mysql.connector


class Carro(abc.ABC):

    __slots__ = ['_placa', '_marca', '_modelo', '_cor', '_cpf', '_acentos']

    def __init__(self, placa, marca, modelo, cor, cpf, acentos):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._cpf = cpf
        self._acentos = acentos

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def acentos(self):
        return self._acentos

    @acentos.setter
    def acentos(self, acentos):
        self._acentos = acentos


class CadCarro:

    __slots__ = ['_conexao', '_cursor', '_mysql']

    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS carros(placa VARCHAR(11) PRIMARY KEY, marca text NOT NULL, modelo text NOT NULL, cor text NOT NULL, cpf VARCHAR(11), acentos integer, foreign key(cpf) references motoristas(cpf));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS reservas(placa VARCHAR(11) PRIMARY KEY, acentos integer, obs_destino text NOT NULL, obs_origem text NOT NULL, destino text NOT NULL, origem text NOT NULL, cpf_cliente VARCHAR(11));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_carro(self, carro):
        existe = self.busca_carro(carro.placa)
        if (existe == None):
            self._cursor.execute('INSERT INTO carros(placa, marca, modelo, cor, cpf, acentos) VALUES(%s,%s,%s,%s,%s,%s)', (carro.placa, carro.marca, carro.modelo, carro.cor, carro.cpf, int(carro.acentos)))
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
            carro = Carro(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5])
            return carro
    
    def busca_carro_cpf(self, cpf):
        self._cursor.execute('SELECT * from carros WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchall()
        if (verificar == None):
            return None
        else:
            carros = []
            for c in verificar:
                car = Carro(c[0], c[1], c[2], c[3], c[4], c[5])
                carros.append(car)
            return carros
        
    def Confirmar_reserva(self, placa, quant_reservas, obs_destino, obs_origem, destino, origem, cpf_cliente):
        existe = self.buscar_reserva(cpf_cliente)
        if (existe == None):
            self._cursor.execute('INSERT INTO reservas(placa, acentos, obs_destino, obs_origem, destino, origem, cpf_cliente) VALUES(%s,%s,%s,%s,%s,%s,%s)', (placa, quant_reservas, obs_destino, obs_origem, destino, origem, cpf_cliente))
            self._conexao.commit()
            self._cursor.execute('UPDATE carros SET acentos = acentos - %s WHERE placa = %s', (quant_reservas, placa))
            self._conexao.commit()
            return True
        else:
            return False
        
    def buscar_reserva(self, cpf_cliente):
        self._cursor.execute('SELECT * from reservas WHERE cpf_cliente = %s',(cpf_cliente,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            return True
