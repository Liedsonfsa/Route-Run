import abc
import mysql.connector


class Reservas(abc.ABC):
    """
    Classe abstrata Reservas responsável por armazenar informações sobre as reservas de viagens.

    ...

    Attributes
    ----------
    placa : str
        Placa do veículo associado à reserva
    acentos : int
        Número de assentos reservados
    obs_destino : str
        Observações sobre o destino da viagem
    obs_origem : str
        Observações sobre a origem da viagem
    destino : str
        Local de destino da viagem
    origem : str
        Local de origem da viagem
    cpf_cliente : str
        CPF do cliente responsável pela reserva

    Methods
    -------
    placa()
        Método que retorna o valor da placa
    placa(placa)
        Método que modifica o valor da placa
    acentos()
        Método que retorna o número de assentos
    acentos(acentos)
        Método que modifica o número de assentos
    obs_destino()
        Método que retorna as observações sobre o destino
    obs_destino(obs_destino)
        Método que modifica as observações sobre o destino
    obs_origem()
        Método que retorna as observações sobre a origem
    obs_origem(obs_origem)
        Método que modifica as observações sobre a origem
    destino()
        Método que retorna o local de destino
    destino(destino)
        Método que modifica o local de destino
    origem()
        Método que retorna o local de origem
    origem(origem)
        Método que modifica o local de origem
    cpf_cliente()
        Método que retorna o CPF do cliente
    cpf_cliente(cpf_cliente)
        Método que modifica o CPF do cliente
    """
    __slots__ = ['_placa', '_acentos', '_obs_destino', '_obs_origem', '_destino', '_origem', '_cpf_cliente']

    def __init__(self, placa, acentos, obs_destino, obs_origem, destino, origem, cpf_cliente):
        """
        Parameters
        ----------
        placa : str
            Placa do veículo associado à reserva
        acentos : int
            Número de assentos reservados
        obs_destino : str
            Observações sobre o destino da viagem
        obs_origem : str
            Observações sobre a origem da viagem
        destino : str
            Local de destino da viagem
        origem : str
            Local de origem da viagem
        cpf_cliente : str
            CPF do cliente responsável pela reserva
        """
        self._placa = placa
        self._acentos = acentos
        self._obs_destino = obs_destino
        self._obs_origem = obs_origem
        self._destino = destino
        self._origem = origem
        self._cpf_cliente = cpf_cliente
    
    @property
    def placa(self):
        '''Retorna a placa associada à reserva.

        ...

        Returns
        -------
        str
            Placa do veículo associado à reserva
        '''
        return self._placa

    @placa.setter
    def placa(self, placa):
        '''Modifica a placa associada à reserva.

        ...

        Parameters
        ----------
        placa : str
            Nova placa do veículo associado à reserva
        '''
        self._placa = placa
    
    @property
    def acentos(self):
        '''Retorna o número de assentos reservados.

        ...

        Returns
        -------
        int
            Número de assentos reservados
        '''
        return self._acentos

    @acentos.setter
    def acentos(self, acentos):
        '''Modifica o número de assentos reservados.

        ...

        Parameters
        ----------
        acentos : int
            Novo número de assentos reservados
        '''
        self._acentos = acentos

    @property
    def obs_destino(self):
        '''Retorna as observações sobre o destino da viagem.

        ...

        Returns
        -------
        str
            Observações sobre o destino da viagem
        '''
        return self._obs_destino

    @obs_destino.setter
    def obs_destino(self, obs_destino):
        '''Modifica as observações sobre o destino da viagem.

        ...

        Parameters
        ----------
        obs_destino : str
            Novas observações sobre o destino da viagem
        '''
        self._obs_destino = obs_destino

    @property
    def obs_origem(self):
        '''Retorna as observações sobre a origem da viagem.

        ...

        Returns
        -------
        str
            Observações sobre a origem da viagem
        '''
        return self._obs_origem

    @obs_origem.setter
    def obs_origem(self, obs_origem):
        '''Modifica as observações sobre a origem da viagem.

        ...

        Parameters
        ----------
        obs_origem : str
            Novas observações sobre a origem da viagem
        '''
        self._obs_origem = obs_origem

    @property
    def destino(self):
        '''Retorna o local de destino da viagem.

        ...

        Returns
        -------
        str
            Local de destino da viagem
        '''
        return self._destino

    @destino.setter
    def destino(self, destino):
        '''Modifica o local de destino da viagem.

        ...

        Parameters
        ----------
        destino : str
            Novo local de destino da viagem
        '''
        self._destino = destino
    
    @property
    def origem(self):
        '''Retorna o local de origem da viagem.

        ...

        Returns
        -------
        str
            Local de origem da viagem
        '''
        return self._origem

    @origem.setter
    def origem(self, origem):
        '''Modifica o local de origem da viagem.

        ...

        Parameters
        ----------
        origem : str
            Novo local de origem da viagem
        '''
        self._origem = origem
    
    @property
    def cpf_cliente(self):
        '''Retorna o CPF do cliente responsável pela reserva.

        ...

        Returns
        -------
        str
            CPF do cliente responsável pela reserva
        '''
        return self._cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, cpf_cliente):
        '''Modifica o CPF do cliente responsável pela reserva.

        ...

        Parameters
        ----------
        cpf_cliente : str
            Novo CPF do cliente responsável pela reserva
        '''
        self._cpf_cliente = cpf_cliente


class Carro(abc.ABC):
    """
    Classe abstrata Carro responsável por armazenar informações sobre os veículos disponíveis.

    ...

    Attributes
    ----------
    placa : str
        Placa do veículo
    marca : str
        Marca do veículo
    modelo : str
        Modelo do veículo
    cor : str
        Cor do veículo
    cpf : str
        CPF do motorista associado ao veículo
    acentos : int
        Número de assentos disponíveis no veículo
    acentos_total : int
        Número total de assentos no veículo

    Methods
    -------
    placa()
        Método que retorna a placa do veículo
    placa(placa)
        Método que modifica a placa do veículo
    marca()
        Método que retorna a marca do veículo
    marca(marca)
        Método que modifica a marca do veículo
    modelo()
        Método que retorna o modelo do veículo
    modelo(modelo)
        Método que modifica o modelo do veículo
    cor()
        Método que retorna a cor do veículo
    cor(cor)
        Método que modifica a cor do veículo
    cpf()
        Método que retorna o CPF do motorista
    cpf(cpf)
        Método que modifica o CPF do motorista
    acentos()
        Método que retorna o número de assentos disponíveis
    acentos(acentos)
        Método que modifica o número de assentos disponíveis
    acentos_total()
        Método que retorna o número total de assentos no veículo
    acentos_total(acentos_total)
        Método que modifica o número total de assentos no veículo
    """
    __slots__ = ['_placa', '_marca', '_modelo', '_cor', '_cpf', '_acentos', '_acentos_total']

    def __init__(self, placa, marca, modelo, cor, cpf, acentos, acentos_total):
        """
        Parameters
        ----------
        placa : str
            Placa do veículo
        marca : str
            Marca do veículo
        modelo : str
            Modelo do veículo
        cor : str
            Cor do veículo
        cpf : str
            CPF do motorista associado ao veículo
        acentos : int
            Número de assentos disponíveis no veículo
        acentos_total : int
            Número total de assentos no veículo
        """
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._cpf = cpf
        self._acentos = acentos
        self._acentos_total = acentos_total

    @property
    def placa(self):
        '''Retorna a placa do veículo.

        ...

        Returns
        -------
        str
            Placa do veículo
        '''
        return self._placa

    @placa.setter
    def placa(self, placa):
        '''Modifica a placa do veículo.

        ...

        Parameters
        ----------
        placa : str
            Nova placa do veículo
        '''
        self._placa = placa

    @property
    def marca(self):
        '''Retorna a marca do veículo.

        ...

        Returns
        -------
        str
            Marca do veículo
        '''
        return self._marca

    @marca.setter
    def marca(self, marca):
        '''Modifica a marca do veículo.

        ...

        Parameters
        ----------
        marca : str
            Nova marca do veículo
        '''
        self._marca = marca

    @property
    def modelo(self):
        '''Retorna o modelo do veículo.

        ...

        Returns
        -------
        str
            Modelo do veículo
        '''
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        '''Modifica o modelo do veículo.

        ...

        Parameters
        ----------
        modelo : str
            Novo modelo do veículo
        '''
        self._modelo = modelo

    @property
    def cor(self):
        '''Retorna a cor do veículo.

        ...

        Returns
        -------
        str
            Cor do veículo
        '''
        return self._cor

    @cor.setter
    def cor(self, cor):
        '''Modifica a cor do veículo.

        ...

        Parameters
        ----------
        cor : str
            Nova cor do veículo
        '''
        self._cor = cor

    @property
    def cpf(self):
        '''Retorna o CPF do motorista associado ao veículo.

        ...

        Returns
        -------
        str
            CPF do motorista associado ao veículo
        '''
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        '''Modifica o CPF do motorista associado ao veículo.

        ...

        Parameters
        ----------
        cpf : str
            Novo CPF do motorista associado ao veículo
        '''
        self._cpf = cpf

    @property
    def acentos(self):
        '''Retorna o número de assentos disponíveis no veículo.

        ...

        Returns
        -------
        int
            Número de assentos disponíveis no veículo
        '''
        return self._acentos

    @acentos.setter
    def acentos(self, acentos):
        '''Modifica o número de assentos disponíveis no veículo.

        ...

        Parameters
        ----------
        acentos : int
            Novo número de assentos disponíveis no veículo
        '''
        self._acentos = acentos
    
    @property
    def acentos_total(self):
        '''Retorna o número total de assentos no veículo.

        ...

        Returns
        -------
        int
            Número total de assentos no veículo
        '''
        return self._acentos_total

    @acentos_total.setter
    def acentos_total(self, acentos_total):
        '''Modifica o número total de assentos no veículo.

        ...

        Parameters
        ----------
        acentos_total : int
            Novo número total de assentos no veículo
        '''
        self._acentos_total = acentos_total


class CadCarro:
    """
    Classe CadCarro responsável por gerenciar o cadastro de carros no banco de dados.

    ...

    Attributes
    ----------
    _conexao : mysql.connector.connection_cext.CMySQLConnection
        Conexão ao banco de dados
    _cursor : mysql.connector.cursor_cext.CMySQLCursor
        Cursor para execução de comandos SQL
    _mysql : str
        Comando SQL para criação das tabelas no banco de dados

    Methods
    -------
    cadastro_carro(carro)
        Cadastra um novo carro no banco de dados
    busca_carro(placa)
        Busca um carro no banco de dados pela placa
    busca_carro_cpf(cpf)
        Busca carros associados a um motorista pelo CPF
    Confirmar_reserva(reserva)
        Confirma uma reserva, atualiza o banco de dados e retorna True se bem-sucedido
    buscar_reserva(cpf_cliente)
        Busca reservas associadas a um cliente pelo CPF
    buscar_reservas_placa(placa)
        Busca reservas associadas a um veículo pela placa
    finalizar_dia(placa, acentosADD)
        Finaliza o dia, atualiza o banco de dados e retorna True se bem-sucedido
    cancelar_reserva(placa, cpf, acentos)
        Cancela uma reserva, atualiza o banco de dados e retorna True se bem-sucedido
    """
    __slots__ = ['_conexao', '_cursor', '_mysql']

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados e cria as tabelas se não existirem.
        """
        self._conexao = mysql.connector.connect(host = 'localhost', db ='route_run', user='root', passwd = '@Marcos2004*')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS carros(placa VARCHAR(11) PRIMARY KEY, marca text NOT NULL, modelo text NOT NULL, cor text NOT NULL, cpf VARCHAR(11), acentos integer, acentos_total integer, foreign key(cpf) references motoristas(cpf));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS reservas(placa VARCHAR(11), acentos integer, obs_destino text NOT NULL, obs_origem text NOT NULL, destino text NOT NULL, origem text NOT NULL, cpf_cliente VARCHAR(11));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
    def cadastro_carro(self, carro):
        """
        Cadastra um novo carro no banco de dados.

        Parameters
        ----------
        carro : Carro
            Objeto da classe Carro contendo as informações do veículo

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False se o veículo já existe no banco de dados
        """
        existe = self.busca_carro(carro.placa)
        if (existe == None):
            self._cursor.execute('INSERT INTO carros(placa, marca, modelo, cor, cpf, acentos, acentos_total) VALUES(%s,%s,%s,%s,%s,%s,%s)', (carro.placa, carro.marca, carro.modelo, carro.cor, carro.cpf, int(carro.acentos), int(carro.acentos_total)))
            self._conexao.commit()
            return True
        else:
            return False

    def busca_carro(self, placa):
        """
        Busca um carro no banco de dados pela placa.

        Parameters
        ----------
        placa : str
            Placa do veículo a ser buscado

        Returns
        -------
        Carro or None
            Objeto da classe Carro se o veículo for encontrado, None se não for encontrado
        """
        self._cursor.execute('SELECT * from carros WHERE placa = %s',(placa,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            carro = Carro(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return carro
    
    def busca_carro_cpf(self, cpf):
        """
        Busca carros associados a um motorista pelo CPF.

        Parameters
        ----------
        cpf : str
            CPF do motorista

        Returns
        -------
        list[Carro]
            Lista de objetos da classe Carro associados ao motorista
        """
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
        """
        Confirma uma reserva, atualiza o banco de dados e retorna True se bem-sucedido.

        Parameters
        ----------
        reserva : Reservas
            Objeto da classe Reservas contendo as informações da reserva

        Returns
        -------
        bool
            True se a reserva foi confirmada com sucesso, False se já existe uma reserva associada ao cliente
        """
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
        """
        Busca reservas associadas a um cliente pelo CPF.

        Parameters
        ----------
        cpf_cliente : str
            CPF do cliente

        Returns
        -------
        list[Reservas] or None
            Lista de objetos da classe Reservas associados ao cliente, None se não houver reservas
        """
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
        """
        Busca reservas associadas a um veículo pela placa.

        Parameters
        ----------
        placa : str
            Placa do veículo

        Returns
        -------
        list[Reservas] or None
            Lista de objetos da classe Reservas associados ao veículo, None se não houver reservas
        """
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
        """
        Finaliza o dia, atualiza o banco de dados e retorna True se bem-sucedido.

        Parameters
        ----------
        placa : str
            Placa do veículo
        acentosADD : int
            Número de assentos a serem adicionados ao veículo

        Returns
        -------
        bool
            True se o dia foi finalizado com sucesso, False se houve algum erro
        """
        self._cursor.execute('UPDATE carros SET acentos = acentos + %s WHERE placa = %s', (acentosADD, placa))
        self._conexao.commit()
        self._cursor.fetchall()
        self._cursor.execute('DELETE from reservas WHERE placa = %s', (placa,))
        self._cursor.fetchall()
        self._conexao.commit()
        return True

    def cancelar_reserva(self, placa, cpf, acentos):
        """
        Cancela uma reserva, atualiza o banco de dados e retorna True se bem-sucedido.

        Parameters
        ----------
        placa : str
            Placa do veículo associado à reserva
        cpf : str
            CPF do cliente associado à reserva
        acentos : int
            Número de assentos reservados a serem devolvidos ao veículo

        Returns
        -------
        bool
            True se a reserva foi cancelada com sucesso, False se houve algum erro
        """
        self._cursor.execute('UPDATE carros SET acentos = acentos + %s WHERE placa = %s', (acentos, placa))
        self._conexao.commit()
        self._cursor.fetchall()
        self._cursor.execute('DELETE from reservas WHERE placa = %s AND cpf_cliente = %s', (placa, cpf))
        self._conexao.commit()
        self._cursor.fetchall()
        return True