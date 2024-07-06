import mercadopago

class Payment_API():
    def __init__(self):
        self.__sdk = mercadopago.SDK("APP_USR-3563203156838220-062116-9b70ab9bd0b6c13d8a3065740cebdbf3-1072601743")
    
    def EfetuarPagamento(self, id, title: str, quantity: int, unit_price: float) -> str:
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }

        payment_data = {
            "items": [
                {
                    "id": str(id),
                    "title": title,
                    "quantity": int(quantity),
                    "currency_id": "BRL",
                    "unit_price": float(unit_price)
                }
            ],
        }

        result = self.__sdk.preference().create(payment_data, 
        request_options)
        payment = result["response"]
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

        payment_response = self.__sdk.payment().create(payment_data, request_options)
        print(payment_response.keys())
        payment = payment_response["response"]
        print(payment.keys())
        print(payment["ticket_url"])

