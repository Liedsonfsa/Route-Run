import abc
import mysql.connector
from datetime import datetime


class Historico(abc.ABC):
    """
    Classe abstrata para representar o histórico de viagens dos motoristas.

    ...

    Attributes
    ----------
    data : datetime
        Data da viagem.
    placa : str
        Placa do veículo.
    origem : str
        Cidade de origem.
    destino : str
        Cidade de destino.
    quantidade_de_acentos : int
        Quantidade de assentos disponíveis.

    Methods
    -------
    data()
        Método que retorna o valor de data.
    data(data)
        Método que modifica o valor de data.
    placa()
        Método que retorna o valor de placa.
    placa(placa)
        Método que modifica o valor de placa.
    origem()
        Método que retorna o valor de origem.
    origem(origem)
        Método que modifica o valor de origem.
    destino()
        Método que retorna o valor de destino.
    destino(destino)
        Método que modifica o valor de destino.
    quantidade_de_acentos()
        Método que retorna o valor de quantidade_de_acentos.
    quantidade_de_acentos(quantidade_de_acentos)
        Método que modifica o valor de quantidade_de_acentos.
    """

    __slots__ = ['_data', '_placa', '_origem', '_destino', '_quantidade_de_acentos']

    def __init__(self, data, placa, origem, destino, quantidade_de_acentos):
        """
        Parameters
        ----------
        data : datetime
            Data da viagem.
        placa : str
            Placa do veículo.
        origem : str
            Cidade de origem.
        destino : str
            Cidade de destino.
        quantidade_de_acentos : int
            Quantidade de assentos disponíveis.
        """
        self._data = data
        self._placa = placa
        self._origem = origem
        self._destino = destino
        self._quantidade_de_acentos = quantidade_de_acentos

    @property
    def data(self):
        '''Realiza o property que retorna o valor de data

        ...

        Returns
        -------
        str
            data do histotico
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''Realiza o setter que modifica o valor de data

        ...

        '''
        self._data = data

    @property
    def placa(self):
        '''Realiza o property que retorna o valor de placa

        ...

        Returns
        -------
        str
            placa do veiculo
        '''
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        '''Realiza o setter que modifica o valor de placa

        ...

        '''
        self._placa = placa
    
    @property
    def origem(self):
        '''Realiza o property que retorna o valor de origem

        ...

        Returns
        -------
        str
            cidade de origem da viagem
        '''
        return self._origem
    
    @origem.setter
    def origem(self, origem):
        '''Realiza o setter que modifica o valor de origem

        ...

        '''
        self._origem = origem 

    @property
    def destino(self):
        '''Realiza o property que retorna o valor de destino

        ...

        Returns
        -------
        str
            cidade de destino da viagem
        '''
        return self._destino
    
    @destino.setter
    def destino(self, destino):
        '''Realiza o setter que modifica o valor de destino

        ...

        '''
        self._destino = destino
    
    @property
    def quantidade_de_acentos(self):
        '''Realiza o property que retorna o valor de quantidade_de_acentos

        ...

        Returns
        -------
        str
            qauntidades de acentos ocupados em determinado dia
        '''
        return self._quantidade_de_acentos
    
    @quantidade_de_acentos.setter
    def quantidade_de_acentos(self, quantidade_de_acentos):
        '''Realiza o setter que modifica o valor de quantidade_de_acentos

        ...

        '''
        self._quantidade_de_acentos = quantidade_de_acentos 


class Rota(abc.ABC):
    """
    Classe abstrata para representar uma rota de viagem.

    ...

    Attributes
    ----------
    id : int
        Identificador único da rota.
    uf_origem : str
        Estado de origem.
    cidade_origem : str
        Cidade de origem.
    uf_destino : str
        Estado de destino.
    cidade_destino : str
        Cidade de destino.
    horario : datetime
        Horário da partida.
    valor : str
        Valor da viagem.
    placa : str
        Placa do veículo.
    horario_volta : datetime
        Horário de retorno.

    Methods
    -------
    id()
        Método que retorna o valor de id.
    id(id)
        Método que modifica o valor de id.
    uf_origem()
        Método que retorna o valor de uf_origem.
    uf_origem(uf_origem)
        Método que modifica o valor de uf_origem.
    cidade_origem()
        Método que retorna o valor de cidade_origem.
    cidade_origem(cidade_origem)
        Método que modifica o valor de cidade_origem.
    horario()
        Método que retorna o valor de horario.
    horario(horario)
        Método que modifica o valor de horario.
    valor()
        Método que retorna o valor de valor.
    valor(valor)
        Método que modifica o valor de valor.
    uf_destino()
        Método que retorna o valor de uf_destino.
    uf_destino(uf_destino)
        Método que modifica o valor de uf_destino.
    cidade_destino()
        Método que retorna o valor de cidade_destino.
    cidade_destino(cidade_destino)
        Método que modifica o valor de cidade_destino.
    placa()
        Método que retorna o valor de placa.
    placa(placa)
        Método que modifica o valor de placa.
    horario_volta()
        Método que retorna o valor de horario_volta.
    horario_volta(horario_volta)
        Método que modifica o valor de horario_volta.
    """

    __slots__ = ['_id', '_uf_origem', '_cidade_origem', '_uf_destino', '_cidade_destino','_horario', '_valor', '_placa', '_horario_volta']

    def __init__(self, id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta):
        """
        Parameters
        ----------
        id : int
            Identificador único da rota.
        uf_origem : str
            Estado de origem.
        cidade_origem : str
            Cidade de origem.
        uf_destino : str
            Estado de destino.
        cidade_destino : str
            Cidade de destino.
        horario : datetime
            Horário da partida.
        valor : str
            Valor da viagem.
        placa : str
            Placa do veículo.
        horario_volta : datetime
            Horário de retorno.
        """
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
        '''Realiza o property que retorna o valor de uf_origem

        ...

        Returns
        -------
        str
            Estado de origem da rota
        '''
        return self._uf_origem
    
    @uf_origem.setter
    def uf_origem(self, uf_origem):
        '''Realiza o setter que modifica o valor de uf_origem

        ...

        Parameters
        ----------
        uf_origem : str
            Novo estado de origem da rota
        '''
        self._uf_origem = uf_origem        
        
    @property
    def cidade_origem(self):
        '''Realiza o property que retorna o valor de cidade_origem

        ...

        Returns
        -------
        str
            Cidade de origem da rota
        '''
        return self._cidade_origem
    
    @cidade_origem.setter
    def cidade_origem(self, cidade_origem):
        '''Realiza o setter que modifica o valor de cidade_origem

        ...

        Parameters
        ----------
        cidade_origem : str
            Nova cidade de origem da rota
        '''
        self._cidade_origem = cidade_origem  
    
    @property
    def horario(self):
        '''Realiza o property que retorna o valor de horario

        ...

        Returns
        -------
        datetime
            Horário da partida da rota
        '''
        return self._horario
    
    @horario.setter
    def horario(self, horario):
        '''Realiza o setter que modifica o valor de horario

        ...

        Parameters
        ----------
        horario : datetime
            Novo horário da partida da rota
        '''
        self._horario = horario   
    
    @property
    def valor(self):
        '''Realiza o property que retorna o valor de valor

        ...

        Returns
        -------
        str
            Valor da viagem da rota
        '''

        return self._valor
    
    @valor.setter
    def valor(self, valor):
        '''Realiza o setter que modifica o valor de valor

        ...

        Parameters
        ----------
        valor : str
            Novo valor da viagem da rota
        '''
        self._valor = valor  

    @property
    def uf_destino(self):
        '''Realiza o property que retorna o valor de uf_destino

        ...

        Returns
        -------
        str
            Estado de destino da rota
        '''
        return self._uf_destino

    @uf_destino.setter
    def uf_destino(self, uf_destino):
        '''Realiza o setter que modifica o valor de uf_destino

        ...

        Parameters
        ----------
        uf_destino : str
            Novo estado de destino da rota
        '''
        self._uf_destino = uf_destino        

    @property
    def cidade_destino(self):
        '''Realiza o property que retorna o valor de cidade_destino

        ...

        Returns
        -------
        str
            Cidade de destino da rota
        '''
        return self._cidade_destino

    @cidade_destino.setter
    def cidade_destino(self, cidade_destino):
        '''Realiza o setter que modifica o valor de cidade_destino

        ...

        Parameters
        ----------
        cidade_destino : str
            Nova cidade de destino da rota
        '''
        self._cidade_destino = cidade_destino

    @property
    def placa(self):
        '''Realiza o property que retorna o valor de placa

        ...

        Returns
        -------
        str
            Placa do veículo da rota
        '''
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        '''Realiza o setter que modifica o valor de placa

        ...

        Parameters
        ----------
        placa : str
            Nova placa do veículo da rota
        '''
        self._placa = placa

    @property
    def id(self):
        '''Realiza o property que retorna o valor de id

        ...

        Returns
        -------
        int
            Identificador único da rota
        '''
        return self._id
    
    @id.setter
    def id(self, id):
        '''Realiza o setter que modifica o valor de id

        ...

        Parameters
        ----------
        id : int
            Novo identificador único da rota
        '''
        self._id = id

    @property
    def horario_volta(self):
        '''Realiza o property que retorna o valor de horario_volta

        ...

        Returns
        -------
        datetime
            Horário de retorno da rota
        '''
        return self._horario_volta
    
    @horario_volta.setter
    def horario_volta(self, horario_volta):
        '''Realiza o setter que modifica o valor de horario_volta

        ...

        Parameters
        ----------
        horario_volta : datetime
            Novo horário de retorno da rota
        '''
        self._horario_volta = horario_volta


class Cidade(abc.ABC):
    """
    Classe abstrata para representar uma cidade.

    ...

    Attributes
    ----------
    id : int
        Identificador único da cidade.
    cidade : str
        Nome da cidade.
    uf_cidade : str
        Estado da cidade.

    Methods
    -------
    id()
        Método que retorna o valor de id.
    id(id)
        Método que modifica o valor de id.
    cidade()
        Método que retorna o valor de cidade.
    cidade(cidade)
        Método que modifica o valor de cidade.
    uf_cidade()
        Método que retorna o valor de uf_cidade.
    uf_cidade(uf_cidade)
        Método que modifica o valor de uf_cidade.
    """
    __slots__ = ['_id', '_cidade', '_uf_cidade']

    def __init__(self, id, cidade, uf_cidade):
        """
        Parameters
        ----------
        id : int
            Identificador único da cidade.
        cidade : str
            Nome da cidade.
        uf_cidade : str
            Estado da cidade.
        """
        self._id = id
        self._cidade = cidade
        self._uf_cidade = uf_cidade

    @property
    def id(self):
        '''Realiza o property que retorna o valor de id

        ...

        Returns
        -------
        int
            Identificador único da cidade
    '''
        return self._id

    @id.setter
    def id(self, id):
        '''Realiza o setter que modifica o valor de id

        ...

        Parameters
        ----------
        id : int
            Novo identificador único da cidade
        '''
        self._id = id

    @property
    def cidade(self):
        '''Realiza o property que retorna o valor de cidade

        ...

        Returns
        -------
        str
            Nome da cidade
        '''
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        '''Realiza o setter que modifica o valor de cidade

        ...

        Parameters
        ----------
        cidade : str
            Novo nome da cidade
        '''
        self._cidade = cidade

    @property
    def uf_cidade(self):
        '''Realiza o property que retorna o valor de uf_cidade

        ...

        Returns
        -------
        str
            Estado da cidade
        '''
        return self._uf_cidade

    @uf_cidade.setter
    def uf_cidade(self, uf_cidade):
        '''Realiza o setter que modifica o valor de uf_cidade

        ...

        Parameters
        ----------
        uf_cidade : str
            Novo estado da cidade
        '''
        self._uf_cidade = uf_cidade


class CadRota:
    """
    Classe para cadastro de rotas e cidades no banco de dados.

    ...

    Attributes
    ----------
    _conexao : object
        Conexão ao banco de dados.
    _cursor : object
        Cursor para executar consultas no banco de dados.
    _mysql : str
        Comandos SQL para criação de tabelas no banco de dados.

    Methods
    -------
    __init__()
        Inicializa a classe e cria tabelas no banco de dados se não existirem.
    cadastro_rota(rota)
        Cadastra uma nova rota no banco de dados.
    contar()
        Conta o número de rotas cadastradas.
    add_city(city)
        Adiciona uma nova cidade no banco de dados.
    buscar_cidade(city)
        Busca uma cidade no banco de dados.
    verificar_cidade(id)
        Verifica se uma cidade existe no banco de dados.
    get_busca(origem)
        Obtém cidades a partir de uma busca.
    verificar_cidade_id(cidade, id, uf_cidade)
        Verifica se uma cidade específica existe no banco de dados.
    add_historico(placa, acentosADD)
        Adiciona um histórico de viagem ao banco de dados.
    buscar_origem_destino(placa)
        Busca a cidade de origem e destino de uma rota específica.
    buscar_histo(placa)
        Busca o histórico de viagens de um motorista no banco de dados.
    """
    __slots__ = ['_conexao', '_cursor', '_mysql']
    
    def __init__(self):
        """
        Inicializa a classe e cria tabelas no banco de dados se não existirem.
        """
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor(buffered=True)
        self._mysql = """CREATE TABLE IF NOT EXISTS rotas(id integer PRIMARY KEY, uf_origem text NOT NULL, cidade_origem text NOT NULL, uf_destino text NOT NULL, cidade_destino text NOT NULL, horario time NOT NULL, valor text NOT NULL, placa text NOT NULL, horario_volta time NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS cidades(id integer, cidade text NOT NULL, uf_cidade text NOT NULL, foreign key(id) references rotas(id));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS historico_mot(data datetime NOT NULL, placa text NOT NULL, origem text NOT NULL, destino text NOT NULL, quantidade_de_acentos integer);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_rota(self, rota):
        '''Realiza o cadastro de uma rota no banco de dados.

        ...

        Parameters
        ----------
        rota : Rota
            Instância da classe Rota contendo os dados da rota a ser cadastrada
        Returns
        -------
        bool
            Retorna True se o cadastro for bem-sucedido, False caso contrário
        '''
        self._cursor.execute('INSERT INTO rotas(id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (rota.id, rota.uf_origem, rota.cidade_origem, rota.uf_destino, rota.cidade_destino, rota.horario.toString("HH:mm:ss"), rota.valor, rota.placa, rota.horario_volta.toString("HH:mm:ss")))
        self._conexao.commit()
        return True

    def contar(self):
        '''Conta o número de rotas cadastradas no banco de dados.

        ...

        Returns
        -------
        int
            Número de rotas cadastradas no banco de dados
        '''
        self._cursor.execute('SELECT COUNT(id) FROM ROTAS')
        verificar = self._cursor.fetchone()
        if verificar != None and len(verificar) > 0:
            count_value = int(verificar[0])
            return count_value
        else:
            return None

    def add_city(self, city):
        '''Adiciona uma cidade ao banco de dados.

        ...

        Parameters
        ----------
        city : Cidade
            Instância da classe Cidade contendo os dados da cidade a ser adicionada
        Returns
        -------
        bool
            Retorna True se a adição for bem-sucedida, False caso contrário
        '''
        existe = self.buscar_cidade(city)

        if (existe == None):
            self._cursor.execute('INSERT INTO cidades(id, cidade, uf_cidade) VALUES(%s,%s,%s)', (city.id, city.cidade, city.uf_cidade))
            self._conexao.commit()
            return True
        else:
            return None

    def buscar_cidade(self, city):
        '''Busca uma cidade no banco de dados.

        ...

        Parameters
        ----------
        city : Cidade
            Instância da classe Cidade contendo os dados da cidade a ser buscada
        Returns
        -------
        Cidade or None
            Retorna a instância da cidade se encontrada, None caso contrário
        '''
        self._cursor.execute('SELECT * from cidades WHERE id = %s AND cidade = %s AND uf_cidade = %s', (city.id, city.cidade, city.uf_cidade,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Cidade(verificar[0], verificar[1], verificar[2])
            return city

    def verificar_cidade(self, id):
        '''Verifica a existência de uma cidade no banco de dados.

        ...

        Parameters
        ----------
        id : int
            Identificador único da cidade a ser verificada
        Returns
        -------
        Rota or None
            Retorna a instância da cidade se encontrada, None caso contrário
        '''
        self._cursor.execute('SELECT * from rotas WHERE id = %s', (id,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Rota(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7], verificar[8])
            return city

    def get_busca(self, origem):
        '''Busca cidades no banco de dados com base na cidade de origem.

        ...

        Parameters
        ----------
        origem : str
            Nome da cidade de origem a ser buscada
        Returns
        -------
        list of Cidade or None
            Retorna uma lista de instâncias de Cidade se encontradas, None caso contrário
        '''
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
        '''Verifica a existência de uma cidade no banco de dados com base em seu identificador, nome e UF.

        ...

        Parameters
        ----------
        cidade : str
            Nome da cidade a ser verificada
        id : int
            Identificador único da cidade a ser verificada
        uf_cidade : str
            UF da cidade a ser verificada
        Returns
        -------
        Cidade or None
            Retorna a instância da cidade se encontrada, None caso contrário
        '''
        self._cursor.execute('SELECT * from cidades WHERE id = %s AND cidade = %s AND uf_cidade = %s', (id,cidade,uf_cidade,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            city = Cidade(verificar[0], verificar[1], verificar[2])
            return city

    def add_historico(self, placa, acentosADD):
        '''Adiciona um histórico de viagem no banco de dados.

        ...

        Parameters
        ----------
        placa : str
            Placa do veículo associado à viagem
        acentosADD : int
            Quantidade de assentos adicionados na viagem
        Returns
        -------
        bool
            Retorna True se a adição for bem-sucedida, False caso contrário
        '''
        origem, destino = self.buscar_origem_destino(placa)
        if origem != None and destino != None:
            data_atual = datetime.now()
            #data_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")
            #print(data_formatada)
            self._cursor.execute('INSERT INTO historico_mot(data, placa, origem, destino, quantidade_de_acentos) VALUES(%s,%s,%s,%s,%s)', (data_atual, placa, origem, destino, acentosADD))
            self._conexao.commit()
            #self._cursor.fetchall()
            return True
        else:
            return False

    def buscar_origem_destino(self, placa):
        '''Busca a cidade de origem e destino associadas a uma placa no banco de dados.

        ...

        Parameters
        ----------
        placa : str
            Placa do veículo associado à viagem
        Returns
        -------
        tuple or None
            Retorna uma tupla contendo a cidade de origem e destino se encontradas, None caso contrário
        '''
        self._cursor.execute('SELECT * from rotas WHERE placa = %s', (placa,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None, None
        else:
            #city = Rota(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7], verificar[8])
            return verificar[2], verificar[4]

    def buscar_histo(self, placa):
        '''Busca o histórico de viagens associado a uma placa no banco de dados.

        ...

        Parameters
        ----------
        placa : str
            Placa do veículo associado à viagem
        Returns
        -------
        list of Historico or None
            Retorna uma lista de instâncias de Historico se encontradas, None caso contrário
        '''
        self._cursor.execute('SELECT * from historico_mot WHERE placa = %s', (placa,))
        verificar = self._cursor.fetchall()

        if (verificar == []):
            return None
        else:
            historicos = []
            for resultado in verificar:
                #print(resultado)
                histo = Historico(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                historicos.append(histo)
            return historicos
