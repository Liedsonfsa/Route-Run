import abc
import mysql.connector


class Rota(abc.ABC):

    __slots__ = ['_id', '_uf_origem', '_cidade_origem', '_uf_destino', '_cidade_destino','_horario', '_valor', '_placa', '_horario_volta']

    def __init__(self, id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta):
        self._id = id
        self._uf_origem = uf_origem
        self._cidade_origem = cidade_origem
        self._uf_destino = uf_destino
        self._cidade_destino = cidade_destino
        self._horario = horario
        self._valor = valor
        self._placa = placa
        self._horario_volta = horario_volta

    @property
    def uf_origem(self):
        return self._uf_origem
    
    @uf_origem.setter
    def uf_origem(self, uf_origem):
        self._uf_origem = uf_origem        
        
    @property
    def cidade_origem(self):
        return self._cidade_origem
    
    @cidade_origem.setter
    def cidade_origem(self, cidade_origem):
        self._cidade_origem = cidade_origem  
    
    @property
    def horario(self):
        return self._horario
    
    @horario.setter
    def horario(self, horario):
        self._horario = horario   
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor  

    @property
    def uf_destino(self):
        return self._uf_destino

    @uf_destino.setter
    def uf_destino(self, uf_destino):
        self._uf_destino = uf_destino        

    @property
    def cidade_destino(self):
        return self._cidade_destino

    @cidade_destino.setter
    def cidade_destino(self, cidade_destino):
        self._cidade_destino = cidade_destino

    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def horario_volta(self):
        return self._horario_volta
    
    @horario_volta.setter
    def horario_volta(self, horario_volta):
        self._horario_volta = horario_volta


class Cidade(abc.ABC):

    __slots__ = ['_id', '_cidade', '_uf_cidade']

    def __init__(self, id, cidade, uf_cidade):
        self._id = id
        self._cidade = cidade
        self._uf_cidade = uf_cidade

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def uf_cidade(self):
        return self._uf_cidade

    @uf_cidade.setter
    def uf_cidade(self, uf_cidade):
        self._uf_cidade = uf_cidade


class CadRota:

    __slots__ = ['_conexao', '_cursor', '_mysql']
    
    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS rotas(id integer PRIMARY KEY, uf_origem text NOT NULL, cidade_origem text NOT NULL, uf_destino text NOT NULL, cidade_destino text NOT NULL, horario time NOT NULL, valor text NOT NULL, placa text NOT NULL, horario_volta time NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS cidades(id integer, cidade text NOT NULL, uf_cidade text NOT NULL, foreign key(id) references rotas(id));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_rota(self, rota):
        self._cursor.execute('INSERT INTO rotas(id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (rota.id, rota.uf_origem, rota.cidade_origem, rota.uf_destino, rota.cidade_destino, rota.horario.toString("HH:mm:ss"), rota.valor, rota.placa, rota.horario_volta.toString("HH:mm:ss")))
        self._conexao.commit()
        return True

    def contar(self):
        self._cursor.execute('SELECT COUNT(id) FROM ROTAS')
        verificar = self._cursor.fetchone()
        if verificar != None and len(verificar) > 0:
            count_value = int(verificar[0])
            return count_value
        else:
            return None

    def add_city(self, city):
        existe = self.buscar_cidade(city)

        if (existe == None):
            self._cursor.execute('INSERT INTO cidades(id, cidade, uf_cidade) VALUES(%s,%s,%s)', (city.id, city.cidade, city.uf_cidade))
            self._conexao.commit()
            return True
        else:
            return None

    def buscar_cidade(self, city):
        self._cursor.execute('SELECT * from cidades WHERE id = %s AND cidade = %s AND uf_cidade = %s', (city.id, city.cidade, city.uf_cidade,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Cidade(verificar[0], verificar[1], verificar[2])
            return city

    def verificar_cidade(self, id):
        self._cursor.execute('SELECT * from rotas WHERE id = %s', (id,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Rota(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7], verificar[8])
            return city

    def get_busca(self, origem):
        self._cursor.execute('SELECT * from cidades WHERE cidade = %s', (origem,))
        verificar = self._cursor.fetchall()

        if (verificar == []):
            return None
        else:
            cidades_origem = []
            for resultado in verificar:
                cidade_origem = Cidade(resultado[0], resultado[1], resultado[2])
                cidades_origem.append(cidade_origem)
            return cidades_origem

    def verificar_cidade_id(self, cidade, id, uf_cidade):
        self._cursor.execute('SELECT * from cidades WHERE id = %s AND cidade = %s AND uf_cidade = %s', (id,cidade,uf_cidade,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Cidade(verificar[0], verificar[1], verificar[2])
            return city
