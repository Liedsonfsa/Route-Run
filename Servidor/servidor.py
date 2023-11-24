from PyQt5.QtCore import QDate, QDateTime, QTime
import socket
from cadastro import Cadastro
from pessoa import Pessoa, Motorista
from cadastro_carro import CadCarro, Carro
from cadastro_rota import Rota, CadRota, Cidade

import threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, con, sinc):
        threading.Thread.__init__(self)
        self.con = con
        self.sinc = sinc
        self._servidor = Servidor()
        print("Nova conexao: ", clientAddress)

    def run(self):
        self.sinc.acquire()
        self._codigo = self.operacao_da_thread()
        self.sinc.release()
        print("Finalizando")

    def operacao_da_thread(self):

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

        self.con.send(saida.encode())
        # print('-solicitacao recebida...')

    @property
    def codigo(self):
        return self._codigo


class Servidor():
    '''
        O objeto da class Servidor representar a interface de conecção do servido com o cliente.
        Todos as informações do objeto são inicializados e inicializando um objeto do tipo cadastro
        um contador de contas cadastradas.
    '''
    def __init__(self):
        self._cadastro = Cadastro()
        self._CadCarro = CadCarro()
        self._rot = CadRota()

    def pre_processamento(self, codigo):
        '''
            Para realizar o pre-processamento do codigo enviado pelo cliente.

            :parametro codigo: string enviada pelo cliente e obtido apos a conecção com o cliente.
            :retorna o codigo_lista, que é o codigo pre processado em formato de lista.
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

        return codigo_lista

    def cadastrarU(self, codigo):
        '''
            Para realizar o cadastro da conta utilizando as informações do codigo recebido pelo cliente e tratado.

            :parametro codigo: lista com informações para cadastro de conta.
            :retorna uma string com '1' para conta realizada, e '0' para conta não realizada.
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
            Para realizar o cadastro da conta utilizando as informações do codigo recebido pelo cliente e tratado.

            :parametro codigo: lista com informações para cadastro de conta.
            :retorna uma string com '1' para conta realizada, e '0' para conta não realizada.
        '''
        data_str = codigo[4]
        data_lista = data_str.split('-')

        qdate = QDate(int(data_lista[0]), int(data_lista[1]), int(data_lista[2]))
        pessoa = Motorista(codigo[1], codigo[2], codigo[3], qdate, codigo[5], codigo[6], codigo[7], codigo[8])
        if(self._cadastro.cadastrar_motorista(pessoa)):
            return '1'
        return '0'

    def buscarCPFcliente(self, codigo):
        cpf = self._cadastro.busca_cpf_cliente(codigo[1])
        if (cpf):
            return f'1/{cpf.nome}/{cpf.endereco}/{cpf.cpf}/{cpf.nascimento}/{cpf.usuario}/{cpf.senha}/{cpf.email}'
        return '0'

    def buscarEMAILcliente(self, codigo):
        email = self._cadastro.buscar_email_user(codigo[1])
        if (email):
            return f'1/{email.nome}/{email.endereco}/{email.cpf}/{email.nascimento}/{email.usuario}/{email.senha}/{email.email}'
        return '0'

    def buscarCPFmot(self, codigo):
        cpf = self._cadastro.busca_cpf_motorista(codigo[1])
        if (cpf):
            return f'1/{cpf.nome}/{cpf.endereco}/{cpf.cpf}/{cpf.nascimento}/{cpf.usuario}/{cpf.senha}/{cpf.email}/{cpf.cnh}'
        return '0'

    def buscarEMAILmot(self, codigo):
        email = self._cadastro.buscar_email_mot(codigo[1])
        if (email):
            return f'1/{email.nome}/{email.endereco}/{email.cpf}/{email.nascimento}/{email.usuario}/{email.senha}/{email.email}/{email.cnh}'
        return '0'

    def redefinirS(self, codigo):
        if self._cadastro.redefinir(codigo[1], codigo[2]):
            return '1'
        return '0'

    def cadastrarC(self, codigo):
        carro = Carro(codigo[1], codigo[2], codigo[3], codigo[4])

        if (self._CadCarro.cadastro_carro(carro)):
            return '1'
        return '0'

    def buscar_carro(self, codigo):
        carro = self._CadCarro.busca_carro(codigo[1])
        if (carro):
            return f'1/{carro.placa}/{carro.tipo}/{carro.modelo}/{carro.cpf}'
        return '0'

    def cont(self):
        ctt = self._rot.contar()
        if (ctt):
            return f'1/{ctt}'
        return '0'

    def Cad_rota(self, codigo):
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
        city = Cidade(int(codigo[1]), codigo[2], codigo[3])

        if (self._rot.add_city(city)):
            return '1'
        return '0'
    
    def GetBusca(self, codigo):
        busca = self._rot.get_busca(codigo[1])
        if (busca):
            if len(busca) >= 1:
                buscaA = f'{busca[0].id}/{busca[0].cidade}/{busca[0].uf_cidade}'
            else:
                buscaA = f'{None}/{None}/{None}/{None}'
            if len(busca) >= 2:
                buscaB = f'{busca[1].id}/{busca[1].cidade}/{busca[1].uf_cidade}'
            else:
                buscaB = f'{None}/{None}/{None}/{None}'
            if len(busca) >= 3:
                buscaC = f'{busca[2].id}/{busca[2].cidade}/{busca[2].uf_cidade}'
            else:
                buscaC = f'{None}/{None}/{None}/{None}'
            if len(busca) >= 4:
                buscaD = f'{busca[3].id}/{busca[3].cidade}/{busca[3].uf_cidade}'
            else:
                buscaD = f'{None}/{None}/{None}/{None}'
            Retorno = f'{buscaA}~{buscaB}~{buscaC}~{buscaD}'
            return f'1-{Retorno}'
        return '0'
    
    def verificarCidadeId(self, codigo):
        city = self._rot.verificar_cidade_id(codigo[1], codigo[2], codigo[3])
        if (city):
            return f'1/{city.cidade}/{city.id}/{city.uf_cidade}'
        return '0'
    
    def verificarCidade(self, codigo):
        city = self._rot.verificar_cidade(int(codigo[1]))
        if (city):
            return f'1/{city.id}/{city.uf_origem}/{city.cidade_origem}/{city.uf_destino}/{city.cidade_destino}/{city.horario}/{city.valor}/{city.placa}/{city.horario_volta}'
        return '0'
    
    def buscaCNH(self, codigo):
        cnh = self._cadastro.busca_cnh(codigo[1])
        if (cnh):
            return f'1/{cnh.nome}/{cnh.endereco}/{cnh.cpf}/{cnh.nascimento}/{cnh.usuario}/{cnh.senha}/{cnh.email}/{cnh.cnh}'
        return '0'

    def ligar_servidor(self):
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
            #print('codigo recebido: {}'.format(codigo))
        #serv_socket.close()