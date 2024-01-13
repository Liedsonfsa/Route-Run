import abc


class Conversa(abc.ABC):
    __slots__ = ['_msg', '_remetente']

    def __init__(self, msg, remetente):
        self._msg = msg
        self._remetente = remetente

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg

    @property
    def remetente(self):
        return self._remetente

    @remetente.setter
    def remetente(self, remetente):
        self._remetente = remetente