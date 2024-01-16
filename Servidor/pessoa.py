import abc


class Pessoa(abc.ABC):
    """
    Classe abstrata Pessoa responsável por receber os atributos dos usuarios clientes

    ...

    Attributes
    ----------
    nome : str
        nome do usuario cliente
    cpf : str
        cpf do usuario cliente
    endereco : str
        endereco do usuario cliente
    nascimento : date
        nascimento do usuario cliente
    usuario : str
        tipo de usuario (cliente)
    senha : str
        senha do usuario cliente
    email : str
        email da conta do usuario cliente

    Methods
    -------
    nome()
        método que retorna o valor de nome
    nome(nome)
        método que modifica o valor de nome
    cpf()
        método que retorna o valor de cpf
    cpf(cpf)
        método que modifica o valor de cpf
    endereco()
        método que retorna o valor de de endereco
    endereco(endereco)
        método que modifica o valor de endereco
    nascimento()
        método que retorna o valor de nascimento
    nascimento(nascimento)
        método que modifica o valor de nascimento
    usuario()
        método que retorna o valor de de usuario
    usuario(usuario)
        método que modifica o valor de usuario
    senha()
        método que retorna o valor de de senha
    senha(senha)
        método que modifica o valor de senha
    email()
        método que retorna o valor de de email
    email(email)
        método que modifica o valor de email
    """

    __slots__ = ['_nome', '_cpf', '_endereco', '_nascimento', '_usuario', '_senha', '_email']

    def __init__(self, nome, endereco, cpf, nascimento, usuario, senha, email):
        """
        Parameters
        ----------
        nome : str
            nome do usuario cliente
        cpf : str
            cpf do usuario cliente
        endereco : str
            endereco do usuario cliente
        nascimento : date
            nascimento do usuario cliente
        usuario : str
            tipo de usuario (cliente)
        senha : str
            senha do usuario cliente
        email : str
            email da conta do usuario cliente
        """

        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento
        self._senha = senha
        self._usuario = usuario
        self._email = email

    @property
    def nome(self):
        '''Realiza o property que retorna o valor de nome

        ...

        Returns
        -------
        str
            nome do usuario cliente
        '''
        return self._nome

    @nome.setter
    def nome(self, nome):
        '''Realiza o setter que modifica o valor de nome

        ...

        '''
        self._nome = nome

    @property
    def cpf(self):
        '''Realiza o property que retorna o valor de cpf

        ...

        Returns
        -------
        str
            cpf do usuario cliente
        '''
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        '''Realiza o setter que modifica o valor de cpf

        ...

        '''
        self._cpf = cpf

    @property
    def endereco(self):
        '''Realiza o property que retorna o valor de endereco

        ...

        Returns
        -------
        str
            endereco do usuario cliente
        '''
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        '''Realiza o setter que modifica o valor de endereco

        ...

        '''
        self._endereco = endereco

    @property
    def nascimento(self):
        '''Realiza o property que retorna o valor de nascimento

        ...

        Returns
        -------
        date
            nascimento do usuario cliente
        '''
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        '''Realiza o setter que modifica o valor de nascimento

        ...

        '''
        self._nascimento = nascimento

    @property
    def senha(self):
        '''Realiza o property que retorna o valor de senha

        ...

        Returns
        -------
        str
            senha do usuario cliente
        '''
        return self._senha

    @senha.setter
    def senha(self, senha):
        '''Realiza o setter que modifica o valor de senha

        ...

        '''
        self._senha = senha

    @property
    def usuario(self):
        '''Realiza o property que retorna o valor de usuario

        ...

        Returns
        -------
        str
            tipo de usuario (cliente)
        '''
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        '''Realiza o setter que modifica o valor de usuario

        ...

        '''
        self._usuario = usuario

    @property
    def email(self):
        '''Realiza o property que retorna o valor de email

        ...

        Returns
        -------
        str
            email da conta do usuario cliente
        '''
        return self._email

    @email.setter
    def email(self, email):
        '''Realiza o setter que modifica o valor de email

        ...

        '''
        self._email = email


class Motorista(Pessoa):
    """
    Classe herdeira Motorista responsável por receber os atributos dos usuarios motoristas. Essa classe herda os atributos da classe peddoa

    ...

    Attributes
    ----------
    nome : str
        nome do usuario motorista
    cpf : str
        cpf do usuario motorista
    endereco : str
        endereco do usuario motorista
    nascimento : date
        nascimento do usuario motorista
    usuario : str
        tipo de usuario (motorista)
    senha : str
        senha do usuario motorista
    email : str
        email da conta do usuario motorista
    cnh : str
        cnh da conta do usuario motorista

    Methods
    -------
    cnh()
        método que retorna o valor de cnh
    cnh(cnh)
        método que modifica o valor de cnh
    """
    def __init__(self, nome, endereco, cpf, nascimento, usuario, senha, email, cnh):
        """
        Parameters
        ----------
        nome : str
            nome do usuario motorista
        cpf : str
            cpf do usuario motorista
        endereco : str
            endereco do usuario motorista
        nascimento : date
            nascimento do usuario motorista
        usuario : str
            tipo de usuario (motorista)
        senha : str
            senha do usuario motorista
        email : str
            email da conta do usuario motorista
        cnh : str
            cnh da conta do usuario motorista
        """
        super().__init__(nome, endereco, cpf, nascimento, usuario, senha, email)
        self._cnh = cnh

    @property
    def cnh(self):
        '''Realiza o property que retorna o valor de cnh

        ...

        Returns
        -------
        str
            cnh do usuario cliente
        '''
        return self._cnh

    @cnh.setter
    def cnh(self, cnh):
        '''Realiza o setter que modifica o valor de cnh

        ...

        '''
        self._cnh = cnh
