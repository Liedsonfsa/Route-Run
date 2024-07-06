import mysql.connector
from pessoa import Pessoa, Motorista
from conversa import Conversa


class Cadastro:
    """
    Classe Cadastro responsável por gerenciar o cadastro de usuários e motoristas, bem como as interações de mensagens entre eles.

    ...

    Attributes
    ----------
    _conexao : obj
        Objeto de conexão ao banco de dados MySQL.
    _cursor : obj
        Objeto de cursor para executar comandos SQL no banco de dados.
    _mysql : str
        String contendo comandos SQL para criação de tabelas no banco de dados.

    Methods
    -------
    __init__()
        Método de inicialização que estabelece a conexão com o banco de dados e cria as tabelas necessárias.
    cadastrar_usuario(pessoa)
        Método para cadastrar um usuário no banco de dados.
    cadastrar_motorista(pessoa)
        Método para cadastrar um motorista no banco de dados.
    busca_cpf_motorista(cpf)
        Método para buscar um motorista pelo CPF no banco de dados.
    busca_cpf_cliente(cpf)
        Método para buscar um cliente pelo CPF no banco de dados.
    busca_cnh(cnh)
        Método para buscar um motorista pela CNH no banco de dados.
    redefinir(email, senha)
        Método para redefinir a senha de um usuário ou motorista.
    editar_perfil_cliente(nome, cpf, endereco, email, nascimento)
        Método para editar o perfil de um cliente no banco de dados.
    editar_perfil_motorista(nome, cpf, endereco, email, nascimento)
        Método para editar o perfil de um motorista no banco de dados.
    buscar_email_mot(email)
        Método para buscar um motorista pelo email no banco de dados.
    buscar_email_user(email)
        Método para buscar um cliente pelo email no banco de dados.
    obter_conversa_id(cpf_remetente, cpf_destinatario)
        Método para obter o ID da conversa entre dois usuários.
    GuardarMSGMot(msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot)
        Método para salvar uma mensagem de um motorista no banco de dados.
    GuardarMSG(msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot)
        Método para salvar uma mensagem de um cliente no banco de dados.
    retirar_msg(cpf_remetente, cpf_destinatario)
        Método para retirar as mensagens de um cliente no banco de dados.
    zerar_mensagens(cpf)
        Método para zerar as mensagens de um cliente no banco de dados.
    zerar_mensagens_mot(cpf)
        Método para zerar as mensagens de um motorista no banco de dados.
    exibir_chats(cpf)
        Método para exibir as conversas de um cliente no banco de dados.
    exibir_chats_mot(cpf)
        Método para exibir as conversas de um motorista no banco de dados.
    retirar_msg_mot(cpf_remetente, cpf_destinatario)
        Método para retirar as mensagens de um motorista no banco de dados.
    """

    __slots__ = ['_conexao', '_cursor', '_mysql']

    def __init__(self):
        """
        Inicializa a classe Cadastro, estabelecendo a conexão com o banco de dados e criando as tabelas necessárias.

        """
        self._conexao = mysql.connector.connect(host='localhost', db='route_run', user='root', passwd='liedsonfsa')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS clientes(nome text NOT NULL, endereco text NOT NULL, cpf VARCHAR(11) PRIMARY KEY, nascimento date NOT NULL, usuario text NOT NULL, senha text NOT NULL, email text NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS motoristas(nome text NOT NULL, endereco text NOT NULL, cpf VARCHAR(11) PRIMARY KEY, nascimento date NOT NULL, usuario text NOT NULL, senha text NOT NULL, email text NOT NULL, cnh text NOT NULL);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS conversas(id VARCHAR(255) PRIMARY KEY);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS mensagens(id VARCHAR(255), msg text NOT NULL, cpf_remetente VARCHAR(11), cpf_destinatario VARCHAR(11), sinal integer, sinal_mot integer, foreign key(id) references conversas(id));"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()

    def cadastrar_usuario(self, pessoa):
        """
        Cadastra um usuário cliente no banco de dados.

        Parameters
        ----------
        pessoa : Pessoa
            Objeto da classe Pessoa contendo os dados do usuário cliente.

        Returns
        -------
        bool
            True se o cadastro for bem-sucedido, False se o CPF já estiver cadastrado.
        """
        existe = self.busca_cpf_cliente(pessoa.cpf)
        
        if (existe == None):
            self._cursor.execute('INSERT INTO clientes(nome,endereco,cpf,nascimento,usuario,senha,email) VALUES(%s,%s,%s,%s,%s,MD5(%s),%s)', (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento.toString("yyyy-MM-dd"), pessoa.usuario, pessoa.senha, pessoa.email))
            self._conexao.commit()
            return True
        else:
            return False

    def cadastrar_motorista(self, pessoa):
        """
        Cadastra um motorista no banco de dados.

        Parameters
        ----------
        pessoa : Motorista
            Objeto da classe Motorista contendo os dados do motorista.

        Returns
        -------
        bool
            True se o cadastro for bem-sucedido, False se o CPF já estiver cadastrado.
        """
        existe = self.busca_cpf_motorista(pessoa.cpf)
        if (existe == None):
            self._cursor.execute('INSERT INTO motoristas(nome,endereco,cpf,nascimento,usuario,senha,email,cnh) VALUES(%s,%s,%s,%s,%s,MD5(%s),%s,%s)', (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento.toString("yyyy-MM-dd"), pessoa.usuario, pessoa.senha, pessoa.email, pessoa.cnh))
            self._conexao.commit()
            return True
        else:
            return False

    def busca_cpf_motorista(self, cpf):
        """
        Busca um motorista pelo CPF no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do motorista a ser buscado.

        Returns
        -------
        Motorista or None
            Objeto da classe Motorista se o CPF for encontrado, None se não existir no banco de dados.
        """
        self._cursor.execute('SELECT * from motoristas WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista

    def busca_cpf_cliente(self, cpf):
        """
        Busca um cliente pelo CPF no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do cliente a ser buscado.

        Returns
        -------
        Pessoa or None
            Objeto da classe Pessoa se o CPF for encontrado, None se não existir no banco de dados.
        """
        self._cursor.execute('SELECT * from clientes WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            pessoa = Pessoa(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return pessoa

    def busca_cnh(self, cnh):
        """
        Busca uma CNH no banco de dados.

        Parameters
        ----------
        cnh : str
            CNH do motorista a ser buscado.

        Returns
        -------
        Motorista or None
            Objeto da classe Motorista se a CNH for encontrada, None se não existir no banco de dados.
        """
        self._cursor.execute('SELECT * from motoristas WHERE cnh = %s',(cnh,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista

    def redefinir(self, email, senha):
        """
        Redefine a senha de um usuário ou motorista no banco de dados.

        Parameters
        ----------
        email : str
            Email do usuário ou motorista.
        senha : str
            Nova senha a ser definida.

        Returns
        -------
        bool or None
            True se a senha for redefinida com sucesso, None se o email não existir no banco de dados.
        """
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
        
    def editar_perfil_cliente(self, nome, cpf, endereco, email, nascimento):
        """
        Edita o perfil de um cliente no banco de dados.

        Parameters
        ----------
        nome : str
            Novo nome do cliente.
        cpf : str
            CPF do cliente.
        endereco : str
            Novo endereço do cliente.
        email : str
            Novo email do cliente.
        nascimento : str
            Nova data de nascimento do cliente.

        Returns
        -------
        bool or None
            True se o perfil for editado com sucesso, None se o CPF não existir no banco de dados.
        """
        conta_user = self.busca_cpf_cliente(cpf)
        conta_mot = self.busca_cpf_motorista(cpf)

        if conta_user is not None:
            self._cursor.execute('UPDATE clientes SET nome = %s, endereco = %s, email = %s, nascimento = %s WHERE cpf = %s', (nome, endereco, email, nascimento.toString("yyyy-MM-dd"), cpf))
        if conta_mot is not None:
            self._cursor.execute('UPDATE motoristas SET nome = %s, endereco = %s, email = %s, nascimento = %s WHERE cpf = %s', (nome, endereco, email, nascimento.toString("yyyy-MM-dd"), cpf))
        self._conexao.commit()
        if conta_user is not None or conta_mot is not None:
            return True
        else:
            return None

    def editar_perfil_motorista(self, nome, cpf, endereco, email, nascimento):
        """
        Edita o perfil de um motorista no banco de dados.

        Parameters
        ----------
        nome : str
            Novo nome do motorista.
        cpf : str
            CPF do motorista.
        endereco : str
            Novo endereço do motorista.
        email : str
            Novo email do motorista.
        nascimento : str
            Nova data de nascimento do motorista.

        Returns
        -------
        bool or None
            True se o perfil for editado com sucesso, None se o CPF não existir no banco de dados.
        """
        conta_user = self.busca_cpf_cliente(cpf)
        conta_mot = self.busca_cpf_motorista(cpf)

        if conta_user is not None:
            self._cursor.execute('UPDATE clientes SET nome = %s, endereco = %s, email = %s, nascimento = %s WHERE cpf = %s', (nome, endereco, email, nascimento.toString("yyyy-MM-dd"), cpf))
        if conta_mot is not None:
            self._cursor.execute('UPDATE motoristas SET nome = %s, endereco = %s, email = %s, nascimento = %s WHERE cpf = %s', (nome, endereco, email, nascimento.toString("yyyy-MM-dd"), cpf))
        self._conexao.commit()
        if conta_user is not None or conta_mot is not None:
            return True
        else:
            return None

    def buscar_email_mot(self, email):
        """
        Busca um motorista pelo email no banco de dados.

        Parameters
        ----------
        email : str
            Email do motorista a ser buscado.

        Returns
        -------
        Motorista or None
            Objeto da classe Motorista se o email for encontrado, None se não existir no banco de dados.
        """
        self._cursor.execute('SELECT * from motoristas WHERE email = %s',(email,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            motorista = Motorista(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6], verificar[7])
            return motorista

    def buscar_email_user(self, email):
        """
        Busca um cliente pelo email no banco de dados.

        Parameters
        ----------
        email : str
            Email do cliente a ser buscado.

        Returns
        -------
        Pessoa or None
            Objeto da classe Pessoa se o email for encontrado, None se não existir no banco de dados.
        """
        self._cursor.execute('SELECT * from clientes WHERE email = %s',(email,))
        verificar = self._cursor.fetchone()
        if (verificar == None):
            return None
        else:
            pessoa = Pessoa(verificar[0], verificar[1], verificar[2], verificar[3], verificar[4], verificar[5], verificar[6])
            return pessoa
        
    def obter_conversa_id(self, cpf_remetente, cpf_destinatario):
        """
        Obtém o ID da conversa entre dois usuários.

        Parameters
        ----------
        cpf_remetente : str
            CPF do remetente.
        cpf_destinatario : str
            CPF do destinatário.

        Returns
        -------
        str
            ID da conversa gerado a partir dos CPFs.
        """
        conversa_id = f"{cpf_remetente}_{cpf_destinatario}"

        # Verifica se o ID da conversa já existe no banco de dados
        self._cursor.execute('SELECT id FROM conversas WHERE id = %s', (conversa_id,))
        resultado = self._cursor.fetchone()

        # Se o ID não existir, insere um novo registro na tabela de conversas
        if resultado is None:
            self._cursor.execute('INSERT INTO conversas(id) VALUES(%s)', (conversa_id,))
            self._conexao.commit()

        return conversa_id

    def GuardarMSGMot(self, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot):
        """
        Salva uma mensagem de um motorista no banco de dados.

        Parameters
        ----------
        msg : str
            Mensagem a ser salva.
        cpf_remetente : str
            CPF do remetente.
        cpf_destinatario : str
            CPF do destinatário.
        sinal : int
            Sinal indicando a visualização do cliente.
        sinal_mot : int
            Sinal indicando a visualização do motorista.
        """
        conversa_id = self.obter_conversa_id(cpf_remetente, cpf_destinatario)

        # Insere a mensagem na tabela de mensagens usando o ID da conversa
        self._cursor.execute('INSERT INTO mensagens(id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot) VALUES(%s,%s,%s,%s,%s,%s)', (conversa_id, msg, cpf_destinatario, cpf_remetente, sinal, sinal_mot))
        self._conexao.commit()

    def GuardarMSG(self, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot):
        """
        Salva uma mensagem de um cliente no banco de dados.

        Parameters
        ----------
        msg : str
            Mensagem a ser salva.
        cpf_remetente : str
            CPF do remetente.
        cpf_destinatario : str
            CPF do destinatário.
        sinal : int
            Sinal indicando a visualização do cliente.
        sinal_mot : int
            Sinal indicando a visualização do motorista.
        """
        conversa_id = self.obter_conversa_id(cpf_remetente, cpf_destinatario)

        # Insere a mensagem na tabela de mensagens usando o ID da conversa
        self._cursor.execute('INSERT INTO mensagens(id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot) VALUES(%s,%s,%s,%s,%s,%s)', (conversa_id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot))
        self._conexao.commit()

    def retirar_msg(self, cpf_remetente, cpf_destinatario):
        """
        Retira as mensagens de um cliente no banco de dados.

        Parameters
        ----------
        cpf_remetente : str
            CPF do remetente.
        cpf_destinatario : str
            CPF do destinatário.

        Returns
        -------
        list or None
            Lista de mensagens retiradas se houver, None se não houver mensagens a serem retiradas.
        """
        conversa_id = f"{cpf_remetente}_{cpf_destinatario}"

        self._cursor.execute('SELECT * from mensagens WHERE id = %s AND sinal = 0',(conversa_id,))
        verificar = self._cursor.fetchall()

        if (verificar == []):
            return None
        else:
            mensagens = []
            #print(verificar)
            for msg in verificar:
                #cidade_origem = Cidade(resultado[0], resultado[1], resultado[2])
                if msg[4] == 0:
                    conversa = Conversa(msg[1], msg[2])
                    mensagens.append(conversa)
                    #print(conversa_id)
                    self._cursor.execute('UPDATE mensagens SET sinal = 1 WHERE id = %s AND sinal = 0', (conversa_id, ))
                    self._conexao.commit()
            return mensagens

    def zerar_mensagens(self, cpf):
        """
        Zera as mensagens de um cliente no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        bool
            True se as mensagens foram zeradas, False se não houver mensagens a serem zeradas.
        """
        #print(cpf)
        self._cursor.execute('SELECT * FROM mensagens WHERE id LIKE %s', (f'{cpf}%',))
        mensagens_a_zerar = self._cursor.fetchall()

        #print("Mensagens a zerar:", mensagens_a_zerar)

        if mensagens_a_zerar:
            # Zerar as mensagens, definindo o campo 'sinal' como 0
            #print("Mensagens a zerar:", mensagens_a_zerar)
            self._cursor.execute('UPDATE mensagens SET sinal = 0 WHERE id LIKE %s', (f'{cpf}%',))
            self._conexao.commit()
            return True
        else:
            return False
        
    def zerar_mensagens_mot(self, cpf):
        """
        Zera as mensagens de um motorista no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do motorista.

        Returns
        -------
        bool
            True se as mensagens foram zeradas, False se não houver mensagens a serem zeradas.
        """
        #print(cpf)
        self._cursor.execute('SELECT * FROM mensagens WHERE id LIKE %s', (f'%{cpf}',))
        mensagens_a_zerar = self._cursor.fetchall()

        #print("Mensagens a zerar:", mensagens_a_zerar)

        if mensagens_a_zerar:
            # Zerar as mensagens, definindo o campo 'sinal' como 0
            #print("Mensagens a zerar:", mensagens_a_zerar)
            self._cursor.execute('UPDATE mensagens SET sinal_mot = 0 WHERE id LIKE %s', (f'%{cpf}',))
            self._conexao.commit()
            return True
        else:
            return False
        
    def exibir_chats(self, cpf):
        """
        Exibe as conversas de um cliente no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        list or None
            Lista de IDs de conversas se houver, None se não houver conversas.
        """
        self._cursor.execute('SELECT * FROM conversas WHERE id LIKE %s', (f'{cpf}%',))
        verificar = self._cursor.fetchall()
        if (verificar == []):
            return None
        else:
            conversas = [x[0] for x in verificar]
            #print(conversas)
            return conversas
        
    def exibir_chats_mot(self, cpf):
        """
        Exibe as conversas de um motorista no banco de dados.

        Parameters
        ----------
        cpf : str
            CPF do motorista.

        Returns
        -------
        list or None
            Lista de IDs de conversas se houver, None se não houver conversas.
        """
        self._cursor.execute('SELECT * FROM conversas WHERE id LIKE %s', (f'%{cpf}',))
        verificar = self._cursor.fetchall()
        if (verificar == []):
            return None
        else:
            conversas = [x[0] for x in verificar]
            #print(conversas)
            return conversas
    
    def retirar_msg_mot(self, cpf_remetente, cpf_destinatario):
        """
        Retira as mensagens de um motorista no banco de dados.

        Parameters
        ----------
        cpf_remetente : str
            CPF do remetente.
        cpf_destinatario : str
            CPF do destinatário.

        Returns
        -------
        list or None
            Lista de mensagens retiradas se houver, None se não houver mensagens a serem retiradas.
        """
        conversa_id = f"{cpf_remetente}_{cpf_destinatario}"

        self._cursor.execute('SELECT * from mensagens WHERE id = %s AND sinal_mot = 0', (conversa_id,))
        verificar = self._cursor.fetchall()

        if (verificar == []):
            return None
        else:
            mensagens = []
            #print(verificar)
            for msg in verificar:

                #cidade_origem = Cidade(resultado[0], resultado[1], resultado[2])
                if msg[5] == 0:
                    conversa = Conversa(msg[1], msg[2])
                    mensagens.append(conversa)
                    #print(conversa_id)
                    self._cursor.execute('UPDATE mensagens SET sinal_mot = 1 WHERE id = %s AND sinal_mot = 0', (conversa_id, ))
                    self._conexao.commit()
            return mensagens
    
    def buscarPreco(self, placa, origem, destino):
        self._cursor.execute('SELECT * FROM rotas WHERE placa = %s AND cidade_origem = %s AND cidade_destino = %s', (placa, origem, destino, ))
        rota = self._cursor.fetchall()
        l = 0
        for i in rota[0]:
            print(i)
            if l == 6 :
                res = i
            l += 1
        
        return float(res.replace(',', '.'))

    def buscarID(self, placa, origem, destino):
        self._cursor.execute('SELECT * FROM rotas WHERE placa = %s AND cidade_origem = %s AND cidade_destino = %s', (placa, origem, destino, ))
        rota = self._cursor.fetchall()
        l = 0
        for i in rota[0]:
            print(i)
            if l == 0:
                res = i
            l += 1
        
        return res
    
    def deletar_veiculo(self, placa):
        self._cursor.execute("SET FOREIGN_KEY_CHECKS=OFF")
        self._cursor.execute('DELETE FROM reservas WHERE placa = %s', (placa, ))

        self._cursor.execute('DELETE FROM historico_mot WHERE placa = %s', (placa, ))

        self._cursor.execute('DELETE FROM rotas WHERE placa = %s', (placa, ))

        self._cursor.execute('DELETE FROM carros WHERE placa = %s', (placa, ))
        self._cursor.execute("SET FOREIGN_KEY_CHECKS=ON")
        
        self._conexao.commit()

        return '1'
    
    def buscar_todas_rotas(self):
        self._cursor.execute("SELECT * FROM rotas")
        rotas = self._cursor.fetchall()

        print(rotas)
        if (rotas == []):
            return None
        
        return rotas
