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
            # "payer":{
            #     "email": "liedsonfsa@gmail.com",
            #     "name": "liedson"
            # }
        }

        result = mercadopago.SDK(self.__access_token).preference().create(payment_data, request_options)
        payment = result["response"]
        # print(payment)
        link_payment = payment["init_point"]
        return link_payment
    
    def PagarComPix(self):
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }

        payment_data = {
            "transaction_amount": 100,
            "description": "Título do produto",
            "payment_method_id": "pix",
            "payer": {
                "email": "fabricoliedson@gmail.com",
                "first_name": "fabricio",
                "last_name": "liedson",
                "identification": {
                    "type": "CPF",
                    "number": "094992793-77"
                },
                "address": {
                    "zip_code": "64565-000",
                    "street_name": "Bairro Antenor Neiva",
                    "street_number": "4",
                    "neighborhood": "Foguete",
                    "city": "Itainópolis",
                    "federal_unit": "PI"
                }
            }
        }

        payment_response = mercadopago.SDK(self.__access_token).payment().create(payment_data, request_options)
        print(payment_response.keys())
        payment = payment_response["response"]
        print(payment.keys())
        print(payment["ticket_url"])


# p = Payment_API()


# r = p.EfetuarPagamento(1, 'teste', 1, 3.45)
# print(r)