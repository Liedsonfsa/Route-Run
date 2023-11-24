import abc


class Pessoa(abc.ABC):

    __slots__ = ['_nome', '_cpf', '_endereco', '_nascimento', '_usuario', '_senha', '_email']

    def __init__(self, nome, endereco, cpf, nascimento, usuario, senha, email):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento
        self._senha = senha
        self._usuario = usuario
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


class Motorista(Pessoa):
    def __init__(self, nome, endereco, cpf, nascimento, usuario, senha, email, cnh):
        super().__init__(nome, endereco, cpf, nascimento, usuario, senha, email)
        self._cnh = cnh
        #self._placa = placa

    @property
    def cnh(self):
        return self._cnh

    @cnh.setter
    def cnh(self, cnh):
        self._cnh = cnh

    '''@property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa'''
