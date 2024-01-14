import abc
import mysql.connector


class Reservas(abc.ABC):

    __slots__ = ['_placa', '_acentos', '_obs_destino', '_obs_origem', '_destino', '_origem', '_cpf_cliente']

    def __init__(self, placa, acentos, obs_destino, obs_origem, destino, origem, cpf_cliente):
        self._placa = placa
        self._acentos = acentos
        self._obs_destino = obs_destino
        self._obs_origem = obs_origem
        self._destino = destino
        self._origem = origem
        self._cpf_cliente = cpf_cliente
    
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa
    
    @property
    def acentos(self):
        return self._acentos

    @acentos.setter
    def acentos(self, acentos):
        self._acentos = acentos

    @property
    def obs_destino(self):
        return self._obs_destino

    @obs_destino.setter
    def obs_destino(self, obs_destino):
        self._obs_destino = obs_destino

    @property
    def obs_origem(self):
        return self._obs_origem

    @obs_origem.setter
    def obs_origem(self, obs_origem):
        self._obs_origem = obs_origem

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino):
        self._destino = destino
    
    @property
    def origem(self):
        return self._origem

    @origem.setter
    def origem(self, origem):
        self._origem = origem
    
    @property
    def cpf_cliente(self):
        return self._cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, cpf_cliente):
        self._cpf_cliente = cpf_cliente


class Carro(abc.ABC):

    __slots__ = ['_placa', '_marca', '_modelo', '_cor', '_cpf', '_acentos', '_acentos_total']

    def __init__(self, placa, marca, modelo, cor, cpf, acentos, acentos_total):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._cpf = cpf
        self._acentos = acentos
        self._acentos_total = acentos_total

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
    
    @property
    def acentos_total(self):
        return self._acentos_total

    @acentos_total.setter
    def acentos_total(self, acentos_total):
        self._acentos_total = acentos_total


class CadCarro:

    __slots__ = ['_conexao', '_cursor', '_mysql']

    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS carros(placa VARCHAR(11) PRIMARY KEY, marca text NOT NULL, modelo text NOT NULL, cor text NOT NULL, cpf VARCHAR(11), acentos integer, acentos_total integer, foreign key(cpf) references motoristas(cpf));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS reservas(placa VARCHAR(11), acentos integer, obs_destino text NOT NULL, obs_origem text NOT NULL, destino text NOT NULL, origem text NOT NULL, cpf_cliente VARCHAR(11));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_carro(self, carro):
        existe = self.busca_carro(carro.placa)
        if (existe == None):
            self._cursor.execute('INSERT INTO carros(placa, marca, modelo, cor, cpf, acentos, acentos_total) VALUES(%s,%s,%s,%s,%s,%s,%s)', (carro.placa, carro.marca, carro.modelo, carro.cor, carro.cpf, int(carro.acentos), int(carro.acentos_total)))
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
            carro = Carro(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return carro
    
    def busca_carro_cpf(self, cpf):
        self._cursor.execute('SELECT * from carros WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchall()
        if (verificar == None):
            return None
        else:
            carros = []
            for c in verificar:
                car = Carro(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
                carros.append(car)
            return carros
        
    def Confirmar_reserva(self, reserva):
        existe = self.buscar_reserva(reserva.cpf_cliente)
        if (existe == None):
            self._cursor.execute('INSERT INTO reservas(placa, acentos, obs_destino, obs_origem, destino, origem, cpf_cliente) VALUES(%s,%s,%s,%s,%s,%s,%s)', (reserva.placa, reserva.acentos, reserva.obs_destino, reserva.obs_origem, reserva.destino, reserva.origem, reserva.cpf_cliente))
            self._conexao.commit()
            self._cursor.fetchall()
            self._cursor.execute('UPDATE carros SET acentos = acentos - %s WHERE placa = %s', (reserva.acentos, reserva.placa))
            self._conexao.commit()
            self._cursor.fetchall()
            return True
        else:
            return False
        
    def buscar_reserva(self, cpf_cliente):
        self._cursor.execute('SELECT * from reservas WHERE cpf_cliente = %s',(cpf_cliente,))
        verificar = self._cursor.fetchall()
        if (verificar == []):
            print('------------------..')
            return None
        else:
            reservas = []
            for r in verificar:
                reserva = Reservas(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                reservas.append(reserva)
            return reservas
        
    def buscar_reservas_placa(self, placa):
        self._cursor.execute('SELECT * from reservas WHERE placa = %s',(placa,))
        verificar = self._cursor.fetchall()
        if (verificar == None):
            return None
        else:
            reservas = []
            for r in verificar:
                reserva = Reservas(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                reservas.append(reserva)
            return reservas
        
    def finalizar_dia(self, placa, acentosADD):
        self._cursor.execute('UPDATE carros SET acentos = acentos + %s WHERE placa = %s', (acentosADD, placa))
        self._conexao.commit()
        self._cursor.fetchall()
        self._cursor.execute('DELETE from reservas WHERE placa = %s', (placa,))
        self._cursor.fetchall()
        self._conexao.commit()
        return True

    def cancelar_reserva(self, placa, cpf, acentos):
        self._cursor.execute('UPDATE carros SET acentos = acentos + %s WHERE placa = %s', (acentos, placa))
        self._conexao.commit()
        self._cursor.fetchall()
        self._cursor.execute('DELETE from reservas WHERE placa = %s AND cpf_cliente = %s', (placa, cpf))
        self._conexao.commit()
        self._cursor.fetchall()
        return True