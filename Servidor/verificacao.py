class Verifica:
    __slots__ = ['_email', '_cod']

    def __init__(self, email, cod):
        self._email = email
        self._cod = cod

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod):
        self._cod = cod