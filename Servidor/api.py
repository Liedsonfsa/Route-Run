import mercadopago
from dotenv import load_dotenv
load_dotenv()

import os

class Payment_API():
    def __init__(self):
        self.__access_token = os.environ['ACCESS_TOKEN']
    
    def EfetuarPagamento(self, id, title: str, quantity: int, unit_price: float) -> str:
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }

        ends = title.split('-')
        msg = f'Realizar pagamento da corrida de {ends[1]} para {ends[2]}'

        payment_data = {
            "items": [
                {
                    "id": str(id),
                    "title": msg,
                    "quantity": int(quantity),
                    "currency_id": "BRL",
                    "unit_price": float(unit_price),
                    "description": "gerando pagamento",
                }
            ],
        }

        result = mercadopago.SDK(self.__access_token).preference().create(payment_data, request_options)
        payment = result["response"]
        # print(payment)
        link_payment = payment["init_point"]
        return link_payment
        
