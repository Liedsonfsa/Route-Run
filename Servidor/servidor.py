from PyQt5.QtCore import QDate, QDateTime, QTime
import socket
from cadastro import Cadastro
from pessoa import Pessoa, Motorista
from cadastro_carro import CadCarro, Carro, Reservas
from cadastro_rota import Rota, CadRota, Cidade

import threading


class ClientThread(threading.Thread):
    '''
    Está classe é utilizada para representar a criação de uma nova thread para o cliente. Ela herda da biblioteca threading

    ...

    Attributes
    ----------
    clientAddress : socket
        É um obejto do tipo soquete que é usado para estabelecer uma conexão cliente em uma rede TCP.
    con : tupla
        É um tupla que recebe o ip do cliente e a porta de conexão
    sinc : Lock
        É um objeto do tipo Lock que é usado para sincronizar o acesso a recursos compartilhados entre threads.
    _servidor : Servidor
        Recebe uma instância da classe Servidor
    
    Methods
    -------
    run()
        Realiza uma operação (definida em operacao_da_thread) de maneira thread-safe, usando um bloqueio para evitar condições de corrida.
    operacao_da_thread()
        Recebe o pacote do cliente e realiza um pré-processamento do pacote (Método da classe Servior).
        Esse pré-processamento redefini a primeira posição do pacote para o nome do método que realizará a função desejada.
        O nome da função é veridicada chamando o método desejado da Classe servidor.
        O retorno do método é reenviado para o cliente com o resultado da sua operação.
    def codigo()
        Realizada o property do objeto codigo
    '''
    def __init__(self, clientAddress, con, sinc):
        '''
        Parameters
        ----------
        clientAddress : socket
            É um obejto do tipo soquete que é usado para estabelecer uma conexão cliente em uma rede TCP.
        con : tupla
            É um tupla que recebe o ip do cliente e a porta de conexão
        sinc : Lock
            É um objeto do tipo Lock que é usado para sincronizar o acesso a recursos compartilhados entre threads.
        '''
        threading.Thread.__init__(self)
        self.con = con
        self.sinc = sinc
        self._servidor = Servidor()
        self._cadastro = Cadastro()
        print("Nova conexao: ", clientAddress)

    def run(self):
        '''Realiza uma operação (definida em operacao_da_thread) de maneira thread-safe

        Realizar alguma operação (definida em operacao_da_thread) de maneira thread-safe, usando um bloqueio (ou semáforo) para evitar condições de corrida.

        '''
        self.sinc.acquire()
        self._codigo = self.operacao_da_thread()
        self.sinc.release()
        print("Finalizando")

    def operacao_da_thread(self):
        '''Método responsável para verificar a operação da thread

        Recebe o pacote do cliente e realiza um pré-processamento do pacote (Método da classe Servior).
        Esse pré-processamento redefini a primeira posição do pacote para o nome do método que realizará a função desejada.
        O nome da função é veridicada chamando o método desejado da Classe servidor.
        O retorno do método é reenviado para o cliente com o resultado da sua operação.

        '''
        #operacoes do servidor
        print('-aguardando solicitacao...')
        recebe = self.con.recv(1024) #define que os pacotes recebidos são de ate 1024 bytes
        
        print('-solicitacao recebida...')

        #pre-processamento do codigo
        codigo = self._servidor.pre_processamento(recebe.decode())
        print(codigo)
    
        if (codigo[0] == 'cadastraU'):
            saida = self._servidor.cadastrarU(codigo)
        elif (codigo[0] == 'buscarCPFcliente'):
            saida = self._servidor.buscarCPFcliente(codigo)
        elif (codigo[0] == 'buscarEMAILcliente'):
            saida = self._servidor.buscarEMAILcliente(codigo)
        elif (codigo[0] == 'cadastraM'):
            saida = self._servidor.cadastrarM(codigo)
        elif (codigo[0] == 'buscarCPFmot'):
            saida = self._servidor.buscarCPFmot(codigo)
        elif (codigo[0] == 'buscarEMAILmot'):
            saida = self._servidor.buscarEMAILmot(codigo)
        elif (codigo[0] == 'redefinir'):
            saida = self._servidor.redefinirS(codigo)
        elif (codigo[0] == 'cadastrarCARRO'):
            saida = self._servidor.cadastrarC(codigo)
        elif (codigo[0] == 'buscarCARRO'):
            saida = self._servidor.buscar_carro(codigo)
        elif (codigo[0] == 'contar'):
            saida = self._servidor.cont()
        elif (codigo[0] == 'cadRota'):
            saida = self._servidor.Cad_rota(codigo)
        elif (codigo[0] == 'cadCity'):
            saida = self._servidor.Cad_city(codigo)
        elif (codigo[0] == 'get_busca'):
            saida = self._servidor.GetBusca(codigo)
        elif (codigo[0] == 'verificarCidadeId'):
            saida = self._servidor.verificarCidadeId(codigo)
        elif (codigo[0] == 'verificarCidade'):
            saida = self._servidor.verificarCidade(codigo)
        elif (codigo[0] == 'buscaCNH'):
            saida = self._servidor.buscaCNH(codigo)
        elif (codigo[0] == 'editarPerfilCliente'):
            saida = self._servidor.EditarPerfilCliente(codigo)
        elif (codigo[0] == 'editarPerfilMotorista'):
            saida = self._servidor.EditarPerfilMotorista(codigo)
        elif (codigo[0] == 'guardarmensagem'):
            saida = self._servidor.Guardar_msg(codigo)
        elif (codigo[0] == 'retirarMsg'):
            saida = self._servidor.RetirarMSG(codigo)
        elif (codigo[0] == 'zerar_mensagens'):
            saida = self._servidor.zerar_mensagens(codigo)
        elif (codigo[0] == 'exibir_chats'):
            saida = self._servidor.exibir_chats(codigo)
        elif (codigo[0] == 'exibir_chats_mot'):
            saida = self._servidor.exibir_chats_mot(codigo)
        elif (codigo[0] == 'zerar_mensagens_mot'):
            saida = self._servidor.zerar_mensagens_mot(codigo)
        elif (codigo[0] == 'guardarmensagem_mot'):
            saida = self._servidor.Guardar_msg_mot(codigo)
        elif (codigo[0] == 'retirarMsgMot'):
            saida = self._servidor.RetirarMSGMot(codigo)
        elif (codigo[0] == 'busca_carro_cpf'):
            saida = self._servidor.busca_carro_cpf(codigo)
        elif (codigo[0] == 'confirmar_reserva'):
            saida = self._servidor.confirmar_reserva(codigo)
        elif (codigo[0] == 'buscar_reservas_placa'):
            saida = self._servidor.buscar_reservas_placa(codigo)
        elif (codigo[0] == 'finalizar_dia'):
            saida = self._servidor.finalizar_dia(codigo)
        elif (codigo[0] == 'buscar_reservas_cpf'):
            saida = self._servidor.buscar_reservas_cpf(codigo)
        elif (codigo[0] == 'cancelar_reserva'):
            saida = self._servidor.cancelar_reserva(codigo)
        elif (codigo[0] == 'buscar_histo'):
            saida = self._servidor.buscar_histo(codigo)
        elif (codigo[0] == 'add_histo'):
            saida = self._servidor.add_histo(codigo)

        self.con.send(saida.encode())
        # print('-solicitacao recebida...')

    @property
    def codigo(self):
        '''Realiza o property do objeto codigo

        ...

        '''
        return self._codigo


class Servidor():
    '''
    O objeto da class Servidor é representar a interface de conexão do servidor com o cliente.

    Todos as informações do objeto são inicializados e inicializando trÊs objetos do tipo: cadastro, cadCarro e CadRota

    Attributes
    ----------
    _cadastro : Cadastro
        Recebe uma instância da Classe Cadastro
    _CadCarro : CadCarro
        Recebe uma instância da Classe CadCarro
    _rot : CadRota
        Recebe uma instância da Classe CadRota

    Methods
    -------
    pre_processamento(codigo)
        Para realizar o pre-processamento do codigo enviado pelo cliente
    cadastrarU(codigo)
        Método responsável por invocar a função cadastrar_usuario da instância cadastro
    cadastrarM(codigo)
        Método responsável por invocar a função cadastrar_motorista da instância cadastro
    buscarCPFcliente(codigo)
        Método responsável por invocar a função busca_cpf_cliente da instância cadastro
    buscarEMAILcliente(codigo)
        Método responsável por invocar a função buscar_email_user da instância cadastro
    buscarCPFmot(codigo)
        Método responsável por invocar a função buscarCPFmot da instância cadastro
    buscarEMAILmot(codigo)
        Método responsável por invocar a função buscarEMAILmot da instância cadastro
    redefinirS(codigo)
        Método responsável por invocar a função redefinir da instância cadastro
    cadastrarC(codigo)
        Método responsável por invocar a função cadastro_carro da instância CadCarro
    buscar_carro(codigo)
        Método responsável por invocar a função buscar_carro da instância CadCarro
    cont(codigo)
        Método responsável por invocar a função contar da instância rot
    Cad_rota(codigo)
        Método responsável por invocar a função cadastro_rota da instância rot
    Cad_city(codigo)
        Método responsável por invocar a função add_city da instância rot
    GetBusca(codigo)
        Método responsável por invocar a função get_busca da instância rot
    verificarCidadeId(codigo)
        Método responsável por invocar a função verificar_cidade_id da instância rot
    verificarCidade(codigo)
        Método responsável por invocar a função verificar_cidade da instância rot
    buscaCNH(codigo)
        Método responsável por invocar a função buscaCNH da instância cadastro
    EditarPerfilCliente(codigo)
        Método responsável por invocar a função editar_perfil_cliente da instância cadastro
    EditarPerfilMotorista(codigo)
        Método responsável por invocar a função editar_perfil_motorista da instância cadastro
    Guardar_msg(codigo)
        Método responsável por invocar a função GuardarMSG da instância cadastro
    RetirarMSG(codigo)
        Método responsável por invocar a função retirar_msg da instância cadastro
    zerar_mensagens(codigo)
        Método responsável por invocar a função zerar_mensagens da instância cadastro
    exibir_chats(codigo)
        Método responsável por invocar a função exibir_chats da instância cadastro
    exibir_chats_mot(codigo)
        Método responsável por invocar a função exibir_chats_mot da instância cadastro
    zerar_mensagens_mot(codigo)
        Método responsável por invocar a função zerar_mensagens_mot da instância cadastro
    Guardar_msg_mot(codigo)
        Método responsável por invocar a função GuardarMSGMot da instância cadastro
    RetirarMSGMot(codigo)
        Método responsável por invocar a função retirar_msg_mot da instância cadastro
    busca_carro_cpf(codigo)
        Método responsável por invocar a função buscar_carro_cpf da instância CadCarro
    confirmar_reserva(codigo)
        Método responsável por invocar a função Confirmar_reserva da instância cadCarro
    buscar_reservas_placa(codigo)
        Método responsável por invocar a função buscar_reservas_carro da instância CadCarro
    finalizar_dia(codigo)
        Método responsável por invocar a função finalizar_dia da instância CadCarro
    add_histo(codigo)
        Método responsável por invocar a função add_historico da instância rot
    buscar_reservas_cpf(codigo)
        Método responsável por invocar a função buscar_reservas_cpf da instância CadCarro
    cancelar_reserva(codigo)
        Método responsável por invocar a função cancelar_reserva da instância CadCarro
    buscar_histo(codigo)
        Método responsável por invocar a função buscar_histo da instância rot
    ligar_servidor(codigo)
        Método responsável por ligar o servidor e ficar aguardando as conexões
    '''
    def __init__(self):
        self._cadastro = Cadastro()
        self._CadCarro = CadCarro()
        self._rot = CadRota()

    def pre_processamento(self, codigo):
        '''
        Realiza o pré_processamento do pacote, troca o número do método pelo seu nome
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente, rota ou carro
        Returns
        -------
        list
            retorna a lista atualizada com o nome do método
        '''
        codigo_lista = codigo.split('/')

        if (codigo_lista[0] == '0'):
            codigo_lista[0] = 'cadastraU'
        elif (codigo_lista[0] == '1'):
            codigo_lista[0] = 'buscarCPFcliente'
        elif (codigo_lista[0] == '2'):
            codigo_lista[0] = 'buscarEMAILcliente'
        elif (codigo_lista[0] == '3'):
            codigo_lista[0] = 'cadastraM'
        elif (codigo_lista[0] == '4'):
            codigo_lista[0] = 'buscarCPFmot'
        elif (codigo_lista[0] == '5'):
            codigo_lista[0] = 'buscarEMAILmot'
        elif (codigo_lista[0] == '6'):
            codigo_lista[0] = 'redefinir'
        elif (codigo_lista[0] == '7'):
            codigo_lista[0] = 'cadastrarCARRO'
        elif (codigo_lista[0] == '8'):
            codigo_lista[0] = 'buscarCARRO'
        elif (codigo_lista[0] == '9'):
            codigo_lista[0] = 'contar'
        elif (codigo_lista[0] == '10'):
            codigo_lista[0] = 'cadRota'
        elif (codigo_lista[0] == '11'):
            codigo_lista[0] = 'cadCity'
        elif (codigo_lista[0] == '12'):
            codigo_lista[0] = 'get_busca'
        elif (codigo_lista[0] == '13'):
            codigo_lista[0] = 'verificarCidadeId'
        elif (codigo_lista[0] == '14'):
            codigo_lista[0] = 'verificarCidade'
        elif (codigo_lista[0] == '15'):
            codigo_lista[0] = 'buscaCNH'
        elif (codigo_lista[0] == '16'):
            codigo_lista[0] = 'editarPerfilCliente'
        elif (codigo_lista[0] == '17'):
            codigo_lista[0] = 'editarPerfilMotorista'
        elif (codigo_lista[0] == '18'):
            codigo_lista[0] = 'guardarmensagem'
        elif (codigo_lista[0] == '19'):
            codigo_lista[0] = 'retirarMsg'
        elif (codigo_lista[0] == '20'):
            codigo_lista[0] = 'zerar_mensagens'
        elif (codigo_lista[0] == '21'):
            codigo_lista[0] = 'exibir_chats'
        elif (codigo_lista[0] == '22'):
            codigo_lista[0] = 'exibir_chats_mot'
        elif (codigo_lista[0] == '23'):
            codigo_lista[0] = 'zerar_mensagens_mot'
        elif (codigo_lista[0] == '24'):
            codigo_lista[0] = 'guardarmensagem_mot'
        elif (codigo_lista[0] == '25'):
            codigo_lista[0] = 'retirarMsgMot'
        elif (codigo_lista[0] == '26'):
            codigo_lista[0] = 'busca_carro_cpf'
        elif (codigo_lista[0] == '27'):
            codigo_lista[0] = 'confirmar_reserva'
        elif (codigo_lista[0] == '28'):
            codigo_lista[0] = 'buscar_reservas_placa'
        elif (codigo_lista[0] == '29'):
            codigo_lista[0] = 'finalizar_dia'
        elif (codigo_lista[0] == '30'):
            codigo_lista[0] = 'buscar_reservas_cpf'
        elif (codigo_lista[0] == '31'):
            codigo_lista[0] = 'cancelar_reserva'
        elif (codigo_lista[0] == '32'):
            codigo_lista[0] = 'buscar_histo'
        elif (codigo_lista[0] == '33'):
            codigo_lista[0] = 'add_histo'          

        return codigo_lista

    def cadastrarU(self, codigo):
        '''
        Realiza a chamada da função cadastrar_usuario da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        data_str = codigo[4]
        data_lista = data_str.split('-')

        # Convertendo para QDate
        qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
        pessoa = Pessoa(codigo[1], codigo[2], codigo[3], qdate, codigo[5], codigo[6], codigo[7])
        if(self._cadastro.cadastrar_usuario(pessoa)):
            return '1'
        return '0'

    def cadastrarM(self, codigo):
        '''
        Método responsável por invocar a função cadastrar_motorista da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        data_str = codigo[4]
        data_lista = data_str.split('-')

        qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
        pessoa = Motorista(codigo[1], codigo[2], codigo[3], qdate, codigo[5], codigo[6], codigo[7], codigo[8])
        if(self._cadastro.cadastrar_motorista(pessoa)):
            return '1'
        return '0'

    def buscarCPFcliente(self, codigo):
        '''
        Método responsável por invocar a função busca_cpf_cliente da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        list
            retorna uma lista com os dados do cliente
        '''
        cpf = self._cadastro.busca_cpf_cliente(codigo[1])
        if (cpf):
            return f'1/{cpf.nome}/{cpf.endereco}/{cpf.cpf}/{cpf.nascimento}/{cpf.usuario}/{cpf.senha}/{cpf.email}'
        return '0'

    def buscarEMAILcliente(self, codigo):
        '''
        Método responsável por invocar a função buscar_email_user da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente

        Returns
        -------
        list
            retorna uma lista com os dados do cliente
        '''
        email = self._cadastro.buscar_email_user(codigo[1])
        if (email):
            return f'1/{email.nome}/{email.endereco}/{email.cpf}/{email.nascimento}/{email.usuario}/{email.senha}/{email.email}'
        return '0'

    def buscarCPFmot(self, codigo):
        '''
        Método responsável por invocar a função buscarCPFmot da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        list
            retorna uma lista com os dados do cliente
        '''
        cpf = self._cadastro.busca_cpf_motorista(codigo[1])
        if (cpf):
            return f'1/{cpf.nome}/{cpf.endereco}/{cpf.cpf}/{cpf.nascimento}/{cpf.usuario}/{cpf.senha}/{cpf.email}/{cpf.cnh}'
        return '0'

    def buscarEMAILmot(self, codigo):
        '''
        Método responsável por invocar a função buscarEMAILmot da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        list
            retorna uma lista com os dados do cliente
        '''
        email = self._cadastro.buscar_email_mot(codigo[1])
        if (email):
            return f'1/{email.nome}/{email.endereco}/{email.cpf}/{email.nascimento}/{email.usuario}/{email.senha}/{email.email}/{email.cnh}'
        return '0'

    def redefinirS(self, codigo):
        '''
        Método responsável por invocar a função redefinir da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da conta cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._cadastro.redefinir(codigo[1], codigo[2]):
            return '1'
        return '0'

    def cadastrarC(self, codigo):
        '''
        Método responsável por invocar a função cadastro_carro da instância CadCarro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do carro
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        carro = Carro(codigo[1], codigo[2], codigo[3], codigo[4], codigo[5], codigo[6], codigo[7])

        if (self._CadCarro.cadastro_carro(carro)):
            return '1'
        return '0'

    def buscar_carro(self, codigo):
        '''
        Método responsável por invocar a função buscar_carro da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do carro
        Returns
        -------
        list
            retorna uma lista com os dados do carro
        '''
        carro = self._CadCarro.busca_carro(codigo[1])
        if (carro):
            return f'1/{carro.placa}/{carro.marca}/{carro.modelo}/{carro.cor}/{carro.cpf}/{carro.acentos}/{carro.acentos_total}'
        return '0'

    def cont(self):
        '''
        Método responsável por invocar a função contar da instância rot
        
        ...

        Returns
        -------
        list
            retorna uma lista com a quantidade de rotas cadastradas
        '''
        ctt = self._rot.contar()
        if (ctt):
            return f'1/{ctt}'
        return '0'

    def Cad_rota(self, codigo):
        '''
        Método responsável por invocar a função cadastro_rota da instância rot
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da rota
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        data_str = codigo[6]
        data_lista = data_str.split(':')
        data_atual = QDate.currentDate()

        # Convertendo para QDate
        qtime = QDateTime(data_atual, QTime(int(data_lista[0]), int(data_lista[1]), int(data_lista[2])))

        data_str1 = codigo[9]
        data_lista1 = data_str1.split(':')
    
        # Convertendo para QDate
        qtime1 = QDateTime(data_atual, QTime(int(data_lista1[0]), int(data_lista1[1]), int(data_lista1[2])))

        rota = Rota(int(codigo[1]), codigo[2], codigo[3], codigo[4], codigo[5], qtime, codigo[7], codigo[8], qtime1)

        if (self._rot.cadastro_rota(rota)):
            return '1'
        return '0'

    def Cad_city(self, codigo):
        '''
        Método responsável por invocar a função add_city da instância rot
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da cidade a ser cadastrada
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        city = Cidade(int(codigo[1]), codigo[2], codigo[3])

        if (self._rot.add_city(city)):
            return '1'
        return '0'
    
    def GetBusca(self, codigo):
        '''
        Método responsável por invocar a função get_busca da instância rot
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da rota
        Returns
        -------
        list
            retorna uma lista com os dados das rotas
        '''
        busca = self._rot.get_busca(codigo[1])
        if (busca):
            tam = len(busca)
            Retorno = []
            for i in range(tam):
                Buscar = f'{busca[i].id}/{busca[i].cidade}/{busca[i].uf_cidade}'
                Retorno.append(Buscar)
            return f'1${Retorno}'
        return '0'
    
    def verificarCidadeId(self, codigo):
        '''
         Método responsável por invocar a função verificar_cidade_id da instância rot
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da cidade
        Returns
        -------
        list
            retorna uma lista com os dados da cidade
        '''
        city = self._rot.verificar_cidade_id(codigo[1], codigo[2], codigo[3])
        if (city):
            return f'1/{city.cidade}/{city.id}/{city.uf_cidade}'
        return '0'
    
    def verificarCidade(self, codigo):
        '''
         Método responsável por invocar a função verificar_cidade da instância rot
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da cidade
        Returns
        -------
        list
            retorna uma lista com os dados da cidade
        '''
        city = self._rot.verificar_cidade(int(codigo[1]))
        if (city):
            return f'1/{city.id}/{city.uf_origem}/{city.cidade_origem}/{city.uf_destino}/{city.cidade_destino}/{city.horario}/{city.valor}/{city.placa}/{city.horario_volta}'
        return '0'
    
    def buscaCNH(self, codigo):
        '''
        Método responsável por invocar a função buscaCNH da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns um número de CNH
        Returns
        -------
        list
            retorna uma lista com os dados do cliente motorista
        '''
        cnh = self._cadastro.busca_cnh(codigo[1])
        if (cnh):
            return f'1/{cnh.nome}/{cnh.endereco}/{cnh.cpf}/{cnh.nascimento}/{cnh.usuario}/{cnh.senha}/{cnh.email}/{cnh.cnh}'
        return '0'
    
    def EditarPerfilCliente(self, codigo):
        '''
        Método responsável por invocar a função editar_perfil_cliente da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        data_str = codigo[5]
        data_lista = data_str.split('-')
    
        # Convertendo para QDate
        qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
        if self._cadastro.editar_perfil_cliente(codigo[1], codigo[2], codigo[3], codigo[4], qdate):
            return '1'
        return '0'
    
    def EditarPerfilMotorista(self, codigo):
        '''
        Método responsável por invocar a função editar_perfil_motorista da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente motorista
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        data_str = codigo[5]
        data_lista = data_str.split('-')
    
        # Convertendo para QDate
        qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
        if self._cadastro.editar_perfil_motorista(codigo[1], codigo[2], codigo[3], codigo[4], qdate):
            return '1'
        return '0'
    
    def Guardar_msg(self, codigo):
        '''
        Método responsável por invocar a função GuardarMSG da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente e cliente morotorista para o armazenamento das mensagens do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._cadastro.GuardarMSG(codigo[1], codigo[2], codigo[3], int(codigo[4]), int(codigo[5])):
            return '1'
        return '0'
    
    def RetirarMSG(self, codigo):
        '''
        Método responsável por invocar a função retirar_msg da instância cadastro
        
        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente e cliente motorista para buscar mensagens do cliente
        Returns
        -------
        list
            retorna uma lista com as mensagens não lidas do cliente.
        '''
        mensagens = self._cadastro.retirar_msg(codigo[1], codigo[2])
        if mensagens:
            tam = len(mensagens)
            Retorno = []
            for i in range(tam):
                Buscar = f'{mensagens[i].msg}/{mensagens[i].remetente}'
                Retorno.append(Buscar)
            return f'1${Retorno}'
        return '0'
    
    def zerar_mensagens(self, codigo):
        '''
        Método responsável por invocar a função zerar_mensagens da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._cadastro.zerar_mensagens(codigo[1]):
            return '1'
        return '0'
    
    def exibir_chats(self, codigo):
        '''
        Método responsável por invocar a função exibir_chats da instância cadastro
 
        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do cliente
        Returns
        -------
        list
            retorna uma lista com todos os chats do cliente
        '''
        conversas = self._cadastro.exibir_chats(codigo[1])
        if conversas:
            return f'1/{conversas}'
        return '0'

    def exibir_chats_mot(self, codigo):
        '''
        Método responsável por invocar a função exibir_chats_mot da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do motorista
        Returns
        -------
        list
            retorna uma lista com todos os chats do motorista
        '''
        conversas = self._cadastro.exibir_chats_mot(codigo[1])
        if conversas:
            return f'1/{conversas}'
        return '0'

    def zerar_mensagens_mot(self, codigo):
        '''
        Método responsável por invocar a função zerar_mensagens_mot da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do motorista
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._cadastro.zerar_mensagens_mot(codigo[1]):
            return '1'
        return '0'
    
    def Guardar_msg_mot(self, codigo):
        '''
        Método responsável por invocar a função GuardarMSGMot da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente e cliente morotorista para o armazenamento das mensagens do cliente motorista
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._cadastro.GuardarMSGMot(codigo[1], codigo[2], codigo[3], int(codigo[4]), int(codigo[5])):
            return '1'
        return '0'

    def RetirarMSGMot(self, codigo):
        '''
        Método responsável por invocar a função retirar_msg_mot da instância cadastro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do cliente e cliente motorista para buscar mensagens do motorista
        Returns
        -------
        list
            retorna uma lista com as mensagens não lidas do motorista
        '''
        mensagens = self._cadastro.retirar_msg_mot(codigo[1], codigo[2])
        if mensagens:
            tam = len(mensagens)
            Retorno = []
            for i in range(tam):
                Buscar = f'{mensagens[i].msg}/{mensagens[i].remetente}'
                Retorno.append(Buscar)
            return f'1${Retorno}'
        return '0'
    
    def busca_carro_cpf(self, codigo):
        '''
        Método responsável por invocar a função buscar_carro_cpf da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do motorista do carro
        Returns
        -------
        list
            retorna uma lista com os dados dos carros
        '''
        carro = self._CadCarro.busca_carro_cpf(codigo[1])
        if (carro):
            tam = len(carro)
            Retorno = []
            for i in range(tam):
                car = f'{carro[i].placa}/{carro[i].marca}/{carro[i].modelo}/{carro[i].cor}/{carro[i].cpf}/{carro[i].acentos}/{carro[i].acentos_total}'
                Retorno.append(car)
            return f'1${Retorno}'
        return '0'
    
    def confirmar_reserva(self, codigo):
        '''
        Método responsável por invocar a função Confirmar_reserva da instância cadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados da reserva feita pelo cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        reserva = Reservas(codigo[1], int(codigo[2]), codigo[3], codigo[4], codigo[5], codigo[6], codigo[7])
        if self._CadCarro.Confirmar_reserva(reserva):
            return '1'
        return '0'
    
    def buscar_reservas_placa(self, codigo):
        '''
        Método responsável por invocar a função buscar_reservas_carro da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com placa do carro
        Returns
        -------
        list
            retorna uma lista com os dados das reservas de um determinado carro
        '''
        reservas = self._CadCarro.buscar_reservas_placa(codigo[1])
        if (reservas):
            tam = len(reservas)
            Retorno = []
            for i in range(tam):
                res = f'{reservas[i].placa}/{reservas[i].acentos}/{reservas[i].obs_destino}/{reservas[i].obs_origem}/{reservas[i].destino}/{reservas[i].origem}/{reservas[i].cpf_cliente}'
                Retorno.append(res)
            return f'1${Retorno}'
        return '0'

    def finalizar_dia(self, codigo):
        '''
        Método responsável por invocar a função finalizar_dia da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do carro
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._CadCarro.finalizar_dia(codigo[1], int(codigo[2])):
            return '1'
        return '0'
    
    def add_histo(self, codigo):
        '''
        Método responsável por invocar a função add_historico da instância rot

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do carro
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        print(codigo[1])
        print(codigo[2])
        if self._rot.add_historico(codigo[1], int(codigo[2])):
            return '1'
        return '0'
    
    def buscar_reservas_cpf(self, codigo):
        '''
        Método responsável por invocar a função buscar_reservas_cpf da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com cpf do cliente
        Returns
        -------
        list
            retorna uma lista com os dados das reservas feitas pelo cliente
        '''
        reservas = self._CadCarro.buscar_reserva(codigo[1])
        if (reservas):
            tam = len(reservas)
            Retorno = []
            for i in range(tam):
                res = f'{reservas[i].placa}/{reservas[i].acentos}/{reservas[i].obs_destino}/{reservas[i].obs_origem}/{reservas[i].destino}/{reservas[i].origem }/{reservas[i].cpf_cliente}'
                Retorno.append(res)
            return f'1${Retorno}'
        return '0'

    def cancelar_reserva(self, codigo):
        '''
        Método responsável por invocar a função cancelar_reserva da instância CadCarro

        ...

        Parameters
        ----------
        codigo : list
            lista com alguns dados do carro e do cliente
        Returns
        -------
        bool
            retorna um boleano (0, 1)
        '''
        if self._CadCarro.cancelar_reserva(codigo[1], codigo[2], codigo[3]):
            return '1'
        return '0'
    
    def buscar_histo(self, codigo):
        '''
        Método responsável por invocar a função buscar_histo da instância rot

        ...

        Parameters
        ----------
        codigo : list
            lista com placa
        Returns
        -------
        list
            retorna uma lista com os historicos de um determinado carro
        '''
        historico = self._rot.buscar_histo(codigo[1])
        if (historico):
            tam = len(historico)
            Retorno = []
            for i in range(tam):
                res = f'{historico[i].data}/{historico[i].placa}/{historico[i].origem}/{historico[i].destino}/{historico[i].quantidade_de_acentos}'
                Retorno.append(res)
            return f'1${Retorno}'
        return '0'

    def ligar_servidor(self):
        '''
        Liga o servidor e fica aguardando as conexões
        
        ...

        '''
        host = ''
        port = 8000
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
        serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
        serv_socket.listen(10) #define o limite de conexões

        sinc = threading.Lock()

        while(True):
            print('-aguardando conexao...')
            con, clientAddress = serv_socket.accept() #servidor aguardando conexão
            print('-coneccao realizada')
            newthread = ClientThread(clientAddress, con, sinc)
            newthread.start()
            newthread.join()
