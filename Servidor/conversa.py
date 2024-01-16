import abc


class Conversa(abc.ABC):
    """
    Classe abstrata Conversa responsável por receber os atributos das mensagens do chat

    ...

    Attributes
    ----------
    msg : str
        Conteudo da mensagem enviada
    remetente : str
        cpf do remetente da mensagem

    Methods
    -------
    msg()
        método que retorna o valor de msg
    msg(msg)
        método que modifica o valor de msg
    remetente()
        método que retorna o valor de remetente
    remetente(remetente)
        método que modifica o valor de remetente
    """
    __slots__ = ['_msg', '_remetente']

    def __init__(self, msg, remetente):
        """
        Parameters
        ----------
        msg : str
            Conteudo da mensagem enviada
        remetente : str
            cpf do remetente da mensagem
        """
        self._msg = msg
        self._remetente = remetente

    @property
    def msg(self):
        '''Realiza o property que retorna o valor de msg

        ...

        Returns
        -------
        str
            Conteudo da mensagem enviada
        '''
        return self._msg

    @msg.setter
    def msg(self, msg):
        '''Realiza o setter que modifica o valor de msg

        ...

        '''
        self._msg = msg

    @property
    def remetente(self):
        '''Realiza o property que retorna o valor de remetente

        ...

        Returns
        -------
        str
            cpf do remetente da mensagem
        '''
        return self._remetente

    @remetente.setter
    def remetente(self, remetente):
        '''Realiza o setter que modifica o valor de remetente

        ...

        '''
        self._remetente = remetente
