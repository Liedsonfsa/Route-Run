from servidor import Servidor


def main():
    '''Função main responsável por chamar o metodo ligar_servidor da instância Servidor.

    Está função é responsavel por ligar o servidor e deixa-lo on-line para conexões

    '''
    servidor = Servidor()
    servidor.ligar_servidor()


if __name__ == "__main__":
    main()
