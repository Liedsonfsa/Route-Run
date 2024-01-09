import mysql.connector
from pessoa import Pessoa, Motorista
from conversa import Conversa


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
        # self._mysql = """CREATE TABLE IF NOT EXISTS clientes_conectados(ip text NOT NULL, porta integer, cpf VARCHAR(11));"""
        # self._cursor.execute(self._mysql)
        # self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS conversas(id VARCHAR(255) PRIMARY KEY);"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        self._mysql = """CREATE TABLE IF NOT EXISTS mensagens(id VARCHAR(255), msg text NOT NULL, cpf_remetente VARCHAR(11), cpf_destinatario VARCHAR(11), sinal integer, sinal_mot integer, foreign key(id) references conversas(id));"""
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
        
    def editar_perfil_cliente(self, nome, cpf, endereco, email, nascimento):
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
        
    def obter_conversa_id(self, cpf_remetente, cpf_destinatario):
    # Concatena os CPFs e ordena para garantir consistência
        #c1, c2 = sorted([cpf_remetente, cpf_destinatario])
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
        conversa_id = self.obter_conversa_id(cpf_remetente, cpf_destinatario)

        # Insere a mensagem na tabela de mensagens usando o ID da conversa
        self._cursor.execute('INSERT INTO mensagens(id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot) VALUES(%s,%s,%s,%s,%s,%s)', (conversa_id, msg, cpf_destinatario, cpf_remetente, sinal, sinal_mot))
        self._conexao.commit()

    def GuardarMSG(self, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot):
        conversa_id = self.obter_conversa_id(cpf_remetente, cpf_destinatario)

        # Insere a mensagem na tabela de mensagens usando o ID da conversa
        self._cursor.execute('INSERT INTO mensagens(id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot) VALUES(%s,%s,%s,%s,%s,%s)', (conversa_id, msg, cpf_remetente, cpf_destinatario, sinal, sinal_mot))
        self._conexao.commit()

    def retirar_msg(self, cpf_remetente, cpf_destinatario):
        #c1, c2 = sorted([cpf_remetente, cpf_destinatario])
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
        # Identificar as mensagens que correspondem ao padrão do CPF
        print(cpf)
        self._cursor.execute('SELECT * FROM mensagens WHERE id LIKE %s', (f'{cpf}%',))
        mensagens_a_zerar = self._cursor.fetchall()

        print("Mensagens a zerar:", mensagens_a_zerar)

        if mensagens_a_zerar:
            # Zerar as mensagens, definindo o campo 'sinal' como 0
            print("Mensagens a zerar:", mensagens_a_zerar)
            self._cursor.execute('UPDATE mensagens SET sinal = 0 WHERE id LIKE %s', (f'{cpf}%',))
            self._conexao.commit()
            return True
        else:
            return False
        
    def zerar_mensagens_mot(self, cpf):
        print(cpf)
        self._cursor.execute('SELECT * FROM mensagens WHERE id LIKE %s', (f'%{cpf}',))
        mensagens_a_zerar = self._cursor.fetchall()

        print("Mensagens a zerar:", mensagens_a_zerar)

        if mensagens_a_zerar:
            # Zerar as mensagens, definindo o campo 'sinal' como 0
            print("Mensagens a zerar:", mensagens_a_zerar)
            self._cursor.execute('UPDATE mensagens SET sinal_mot = 0 WHERE id LIKE %s', (f'%{cpf}',))
            self._conexao.commit()
            return True
        else:
            return False
        
    def exibir_chats(self, cpf):
        self._cursor.execute('SELECT * FROM conversas WHERE id LIKE %s', (f'{cpf}%',))
        verificar = self._cursor.fetchall()
        if (verificar == []):
            return None
        else:
            conversas = [x[0] for x in verificar]
            #print(conversas)
            return conversas
        
    def exibir_chats_mot(self, cpf):
        self._cursor.execute('SELECT * FROM conversas WHERE id LIKE %s', (f'%{cpf}',))
        verificar = self._cursor.fetchall()
        if (verificar == []):
            return None
        else:
            conversas = [x[0] for x in verificar]
            #print(conversas)
            return conversas
    
    def retirar_msg_mot(self, cpf_remetente, cpf_destinatario):
        #c1, c2 = sorted([cpf_remetente, cpf_destinatario])
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
