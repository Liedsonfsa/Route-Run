import socket
import threading
from mysql.connector.utils import print_buffer


class plataforma_cliente():
    """
    Classe plataforma_cliente responsável por gerenciar todas as funcionalidades da aplicação

    ...

    Attributes
    ----------
    _listas_contas : list
        lista para guardar os numeros para recuperação de senha

    Methods
    -------
    conecxao_servidor(codigo)
        Estabelece uma conexão com o servidor e envia um código.
    cadastro_user(nome, endereco, cpf, nascimento, usuario, senha, email)
        Realiza o cadastro de um usuário.
    busca_cpf_cliente(cpf)
        Busca um cliente pelo CPF.
    buscar_email_cliente(email)
        Busca um cliente pelo endereço de e-mail.
    cadastro_mot(nome, endereco, cpf, nascimento, usuario, senha, email, cnh)
        Realiza o cadastro de um motorista.
    busca_cpf_mot(cpf)
        Busca um motorista pelo CPF.
    buscar_email_mot(email)
        Busca um motorista pelo email.
    guardar_num(cod)
        Guarda um número na lista de contas.
    buscar_cod(cod)
        Busca um código na lista de contas.
    redefinir(email, senha)
        Redefine a senha de um usuário.
    cadastrar_carro(placa, marca, modelo, cor, cpf, acentos)
        Cadastra um novo carro.
    busca_carro(placa)
        Busca um carro pela placa.
    contar()
        Conta o número de registros no sistema.
    cadastro_rota(id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta)
        Cadastra uma nova rota.
    add_city(id, cidade, uf)
        Adiciona uma cidade ao sistema.
    get_busca(cidade)
        Realiza uma busca com base na cidade.
    verificar_cidade_id(cidade, id, uf_cidade)
        Verifica se uma cidade específica existe no banco de dados.
    verificar_cidade(id)
        Verifica se uma cidade existe no banco de dados.
    busca_cnh(cnh)
        Realiza uma busca com base no número da CNH.
    editar_perfil_cliente(nome, cpf, endereco, email, nascimento)
        Edita o perfil de um cliente.
    editar_perfil_motorista(nome, cpf, endereco, email, nascimento)
        Edita o perfil de um motorista.
    guardar_msg(msg, remetente, destinatario, sinal, sinal_mot)
        Guarda uma mensagem no servidor.
    retirar_msg(remetente, destinatario)
        Retira mensagens entre remetente e destinatário.
    zerar_mensagens(cpf)
        Zera as mensagens de um cliente.
    exibir_chats(cpf)
        Exibe os chats de um cliente.
    exibir_chats_mot(cpf)
        Exibe os chats de um motorista.
    zerar_mensagens_mot(cpf)
        Zera as mensagens de um motorista.
    guardar_msg_mot(msg, remetente, destinatario, sinal, sinal_mot)
        Guarda uma mensagem no servidor para motoristas.
    retirar_msg_mot(remetente, destinatario)
        Retira mensagens entre remetente e destinatário para motoristas.
    busca_carro_cpf(cpf)
        Realiza uma busca de carro com base no CPF do motorista.
    confirmar_reserva(placa, quant_reservas, obs_destino, obs_origem, destino, origem, cpf_cliente)
        Confirma uma reserva.
    buscar_reservas_placa(placa)
        Busca reservas por placa.
    finalizar_dia(placa, acentosADD)
        Finaliza o dia de um motorista.
    buscar_reservas_cpf(cpf)
        Busca reservas por CPF.
    cancelar_reserva(placa, cpf, acentos)
        Cancela uma reserva.
    buscar_histo(placa)
        Busca o histórico de viagens de um motorista.
    add_histo(placa, acentosADD)
        Adiciona um histórico de viagem.
    """
    def __init__(self):
        self._lista_contas = []

    def conecxao_servidor(self, codigo):
        """
        Estabelece uma conexão com o servidor e envia um código.

        Parameters
        ----------
        codigo : str
            Código a ser enviado para o servidor.

        Returns
        -------
        str
            Resposta do servidor.
        """
        ip = '10.180.46.216'
        port = 8000
        addr = ((ip, port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        client_socket.send(codigo.encode())
        print('entrada: '+codigo)
        saida = client_socket.recv(1024).decode()
        client_socket.close()

        return saida

    def cadastro_user(self, nome, endereco, cpf, nascimento, usuario, senha, email):
        """
        Realiza o cadastro de um usuário.

        Parameters
        ----------
        nome : str
            Nome do usuário.
        endereco : str
            Endereço do usuário.
        cpf : str
            CPF do usuário.
        nascimento : datetime
            Data de nascimento do usuário.
        usuario : str
            Nome de usuário.
        senha : str
            Senha do usuário.
        email : str
            Endereço de e-mail do usuário.

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
        codigo = '0/'+nome+'/'+endereco+'/'+cpf+'/'+nascimento.toString("yyyy-MM-dd")+'/'+usuario+'/'+senha+'/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return False
    
    def busca_cpf_cliente(self, cpf):
        """
        Busca um cliente pelo CPF.

        Parameters
        ----------
        cpf : str
            CPF do cliente a ser buscado.

        Returns
        -------
        list or None
            Lista com informações do cliente se encontrado, None caso contrário.
        """
        codigo = '1/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def buscar_email_cliente(self, email):
        """
        Busca um cliente pelo endereço de e-mail.

        Parameters
        ----------
        email : str
            Endereço de e-mail do cliente a ser buscado.

        Returns
        -------
        list or None
            Lista com informações do cliente se encontrado, None caso contrário.
        """
        codigo = '2/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def cadastro_mot(self, nome, endereco, cpf, nascimento, usuario, senha, email, cnh):
        """
        Realiza o cadastro de um motorista.

        Parameters
        ----------
        nome : str
            Nome do motorista.
        endereco : str
            Endereço do motorista.
        cpf : str
            CPF do motorista.
        nascimento : datetime
            Data de nascimento do motorista.
        usuario : str
            Nome de usuário do motorista.
        senha : str
            Senha do motorista.
        email : str
            Endereço de e-mail do motorista.
        cnh : str
            Número da CNH do motorista.

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
        codigo = '3/'+nome+'/'+endereco+'/'+cpf+'/'+nascimento.toString("yyyy-MM-dd")+'/'+usuario+'/'+senha+'/'+email+'/'+cnh
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def busca_cpf_mot(self, cpf):
        """
        Busca um motorista pelo CPF.

        Parameters
        ----------
        cpf : str
            CPF do motorista a ser buscado.

        Returns
        -------
        list or None
            Lista com informações do motorista se encontrado, None caso contrário.
        """
        codigo = '4/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def buscar_email_mot(self, email):
        """
        Busca um motorista pelo endereço de e-mail.

        Parameters
        ----------
        email : str
            Endereço de e-mail do motorista a ser buscado.

        Returns
        -------
        list or None
            Lista com informações do motorista se encontrado, None caso contrário.
        """
        codigo = '5/'+email
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def guardar_num(self, cod):
        """
        Guarda um número na lista de contas.

        Parameters
        ----------
        cod : str
            Número a ser guardado.
        """
        self._lista_contas.clear()
        self._lista_contas.append(cod)

    def buscar_cod(self, cod):
        """
        Busca um código na lista de contas.

        Parameters
        ----------
        cod : str
            Código a ser buscado.

        Returns
        -------
        str or None
            O código se encontrado, None caso contrário.
        """
        for num in self._lista_contas:
            if num == cod:
                return num
        return None

    def redefinir(self, email, senha):
        """
        Redefine a senha de um usuário.

        Parameters
        ----------
        email : str
            Endereço de e-mail do usuário.
        senha : str
            Nova senha do usuário.

        Returns
        -------
        bool
            True se a redefinição foi bem-sucedida, False caso contrário.
        """
        codigo = '6/'+email+'/'+senha
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def cadastrar_carro(self, placa, marca, modelo, cor, cpf, acentos):
        """
        Cadastra um novo carro.

        Parameters
        ----------
        placa : str
            Placa do carro.
        marca : str
            Marca do carro.
        modelo : str
            Modelo do carro.
        cor : str
            Cor do carro.
        cpf : str
            CPF do proprietário do carro.
        acentos : int
            Número total de assentos no carro.

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
        codigo = '7/'+placa+'/'+marca+'/'+modelo+'/'+cor+'/'+cpf+'/'+str(acentos)+'/'+str(acentos)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def busca_carro(self, placa):
        """
        Busca um carro pela placa.

        Parameters
        ----------
        placa : str
            Placa do carro a ser buscado.

        Returns
        -------
        list or None
            Lista com informações do carro se encontrado, None caso contrário.
        """
        codigo = '8/'+placa
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def contar(self):
        """
        Conta o número de registros no sistema.

        Returns
        -------
        int or None
            Número total de registros se obtido com sucesso, None caso contrário.
        """
        codigo = '9/'
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return int(saida_lst[1])
        return None
    
    def cadastro_rota(self, id, uf_origem, cidade_origem, uf_destino, cidade_destino, horario, valor, placa, horario_volta):
        """
        Cadastra uma nova rota.

        Parameters
        ----------
        id : int
            Identificador da rota.
        uf_origem : str
            UF de origem da rota.
        cidade_origem : str
            Cidade de origem da rota.
        uf_destino : str
            UF de destino da rota.
        cidade_destino : str
            Cidade de destino da rota.
        horario : datetime
            Horário de partida da rota.
        valor : str
            Valor da rota.
        placa : str
            Placa do carro associado à rota.
        horario_volta : datetime
            Horário de volta da rota.

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
        codigo = '10/'+str(id)+'/'+uf_origem+'/'+cidade_origem+'/'+uf_destino+'/'+cidade_destino+'/'+horario.toString("HH:mm:ss")+'/'+valor+'/'+placa+'/'+horario_volta.toString("HH:mm:ss")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def add_city(self, id, cidade, uf):
        """
        Adiciona uma cidade ao sistema.

        Parameters
        ----------
        id : int
            Identificador da cidade.
        cidade : str
            Nome da cidade.
        uf : str
            UF da cidade.

        Returns
        -------
        bool
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
        codigo = '11/'+str(id)+'/'+cidade+'/'+uf

        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def get_busca(self, cidade):
        """
        Obtém cidades a partir de uma busca.

        Parameters
        ----------
        cidade : str
            Cidade a ser buscada.

        Returns
        -------
        list or None
            Lista com cidades encontradas, None caso não haja resultados.
        """
        codigo = '12/'+cidade
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None

    def verificar_cidade_id(self, cidade, id, uf_cidade):
        """
        Verifica se uma cidade específica existe no banco de dados.

        Parameters
        ----------
        cidade : str
            Nome da cidade.
        id : int
            ID da cidade.
        uf_cidade : str
            UF da cidade.

        Returns
        -------
        list or None
            Lista com informações da cidade se encontrada, None caso contrário.
        """
        codigo = '13/'+cidade+'/'+str(id)+'/'+uf_cidade
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def verificar_cidade(self, id):
        """
        Verifica se uma cidade existe no banco de dados.

        Parameters
        ----------
        id : int
            ID da cidade.

        Returns
        -------
        list or None
            Lista com informações da cidade se encontrada, None caso contrário.
        """
        codigo = '14/'+str(id)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None
    
    def busca_cnh(self, cnh):
        """
        Busca um motorista pelo número da CNH.

        Parameters
        ----------
        cnh : str
            Número da CNH do motorista.

        Returns
        -------
        list or None
            Lista com informações do motorista se encontrado, None caso contrário.
        """
        codigo = '15/'+cnh
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst
        return None

    def editar_perfil_cliente(self, nome, cpf, endereco, email, nascimento):
        """
        Edita o perfil de um cliente.

        Parameters
        ----------
        nome : str
            Novo nome do cliente.
        cpf : str
            CPF do cliente.
        endereco : str
            Novo endereço do cliente.
        email : str
            Novo e-mail do cliente.
        nascimento : datetime
            Nova data de nascimento do cliente.

        Returns
        -------
        bool
            True se a edição foi bem-sucedida, False caso contrário.
        """
        codigo = '16/'+nome+'/'+cpf+'/'+endereco+'/'+email+'/'+nascimento.toString("yyyy-MM-dd")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def editar_perfil_motorista(self, nome, cpf, endereco, email, nascimento):
        """
        Edita o perfil de um motorista.

        Parameters
        ----------
        nome : str
            Novo nome do motorista.
        cpf : str
            CPF do motorista.
        endereco : str
            Novo endereço do motorista.
        email : str
            Novo e-mail do motorista.
        nascimento : datetime
            Nova data de nascimento do motorista.

        Returns
        -------
        bool
            True se a edição foi bem-sucedida, False caso contrário.
        """
        codigo = '17/'+nome+'/'+cpf+'/'+endereco+'/'+email+'/'+nascimento.toString("yyyy-MM-dd")
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def guardar_msg(self, msg, remetente, destinatario, sinal, sinal_mot):
        """
        Armazena uma mensagem no servidor.

        Parameters
        ----------
        msg : str
            Mensagem a ser armazenada.
        remetente : str
            Remetente da mensagem.
        destinatario : str
            Destinatário da mensagem.
        sinal : int
            Sinal indicando o tipo de mensagem.
        sinal_mot : int
            Sinal indicando se a mensagem é destinada a um motorista.

        Returns
        -------
        bool
            True se a mensagem foi armazenada com sucesso, False caso contrário.
        """
        codigo = '18/'+msg+'/'+remetente+'/'+destinatario+'/'+str(sinal)+'/'+str(sinal_mot)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
        
    def retirar_msg(self, remetente, destinatario):
        """
        Recupera mensagens do servidor.

        Parameters
        ----------
        remetente : str
            Remetente das mensagens.
        destinatario : str
            Destinatário das mensagens.

        Returns
        -------
        list or None
            Lista com mensagens encontradas, None caso não haja mensagens.
        """
        codigo = '19/'+remetente+'/'+destinatario
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None
    
    def zerar_mensagens(self, cpf):
        """
        Zera as mensagens de um cliente no servidor.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        bool
            True se as mensagens foram zeradas com sucesso, False caso contrário.
        """
        codigo = '20/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def exibir_chats(self, cpf):
        """
        Exibe os chats de um cliente.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        list or None
            Lista com chats encontrados, None caso não haja chats.
        """
        codigo = '21/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None
    
    def exibir_chats_mot(self, cpf):
        """
        Exibe os chats de um motorista.

        Parameters
        ----------
        cpf : str
            CPF do motorista.

        Returns
        -------
        list or None
            Lista com chats encontrados, None caso não haja chats.
        """
        codigo = '22/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None

    def zerar_mensagens_mot(self, cpf):
        """
        Zera as mensagens de um motorista no servidor.

        Parameters
        ----------
        cpf : str
            CPF do motorista.

        Returns
        -------
        bool
            True se as mensagens foram zeradas com sucesso, False caso contrário.
        """
        codigo = '23/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def guardar_msg_mot(self, msg, remetente, destinatario, sinal, sinal_mot):
        """
        Armazena uma mensagem destinada a um motorista no servidor.

        Parameters
        ----------
        msg : str
            Mensagem a ser armazenada.
        remetente : str
            Remetente da mensagem.
        destinatario : str
            Destinatário da mensagem.
        sinal : int
            Sinal indicando o tipo de mensagem.
        sinal_mot : int
            Sinal indicando se a mensagem é destinada a um motorista.

        Returns
        -------
        bool
            True se a mensagem foi armazenada com sucesso, False caso contrário.
        """
        codigo = '24/'+msg+'/'+remetente+'/'+destinatario+'/'+str(sinal)+'/'+str(sinal_mot)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def retirar_msg_mot(self, remetente, destinatario):
        """
        Recupera mensagens destinadas a um motorista do servidor.

        Parameters
        ----------
        remetente : str
            Remetente das mensagens.
        destinatario : str
            Destinatário das mensagens.

        Returns
        -------
        list or None
            Lista com mensagens encontradas, None caso não haja mensagens.
        """
        codigo = '25/'+remetente+'/'+destinatario
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None

    def busca_carro_cpf(self, cpf):
        """
        Busca carros associados a um CPF no servidor.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        list or None
            Lista com informações dos carros associados ao CPF, None caso não haja carros.
        """
        codigo = '26/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None

    def confirmar_reserva(self, placa, quant_reservas, obs_destino, obs_origem, destino, origem, cpf_cliente):
        """
        Confirma uma reserva no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.
        quant_reservas : int
            Quantidade de reservas.
        obs_destino : str
            Observações sobre o destino.
        obs_origem : str
            Observações sobre a origem.
        destino : str
            Destino da reserva.
        origem : str
            Origem da reserva.
        cpf_cliente : str
            CPF do cliente.

        Returns
        -------
        bool
            True se a reserva foi confirmada com sucesso, False caso contrário.
        """
        codigo = '27/'+placa+'/'+str(quant_reservas)+'/'+obs_destino+'/'+obs_origem+'/'+destino+'/'+origem+'/'+cpf_cliente
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def buscar_reservas_placa(self, placa):
        """
        Busca reservas associadas a uma placa no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.

        Returns
        -------
        list or None
            Lista com informações das reservas encontradas, None caso não haja reservas.
        """
        codigo = '28/'+placa
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        return None
    
    def finalizar_dia(self, placa, acentosADD):
        """
        Finaliza o dia de um motorista no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.
        acentosADD : int
            Número de assentos adicionais.

        Returns
        -------
        bool
            True se o dia foi finalizado com sucesso, False caso contrário.
        """
        codigo = '29/'+placa+'/'+str(acentosADD)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None

    def buscar_reservas_cpf(self, cpf):
        """
        Busca reservas associadas a um CPF no servidor.

        Parameters
        ----------
        cpf : str
            CPF do cliente.

        Returns
        -------
        list or None
            Lista com informações das reservas encontradas, None caso não haja reservas.
        """
        codigo = '30/'+cpf
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')

    def cancelar_reserva(self, placa, cpf, acentos):
        """
        Cancela uma reserva no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.
        cpf : str
            CPF do cliente.
        acentos : int
            Número de assentos.

        Returns
        -------
        bool
            True se a reserva foi cancelada com sucesso, False caso contrário.
        """
        codigo = '31/'+placa+'/'+cpf+'/'+acentos
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
    
    def buscar_histo(self, placa):
        """
        Busca o histórico de viagens de um motorista no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.

        Returns
        -------
        list or None
            Lista com informações do histórico de viagens encontradas, None caso não haja histórico.
        """
        codigo = '32/'+placa
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('$')
        if (saida_lst[0] == '1'):
            return saida_lst[1].split(',')
        
    def add_histo(self, placa, acentosADD):
        """
        Adiciona um histórico de viagem no servidor.

        Parameters
        ----------
        placa : str
            Placa do veículo.
        acentosADD : int
            Número de assentos adicionais.

        Returns
        -------
        bool
            True se o histórico de viagem foi adicionado com sucesso, False caso contrário.
        """
        codigo = '33/'+placa+'/'+str(acentosADD)
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if (saida_lst[0] == '1'):
            return True
        return None
