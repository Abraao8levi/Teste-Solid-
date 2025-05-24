# aqui vai o código está  problematico,pois ocorre :
# PaymentProcessor tá fazendo tudo: processa pagamento e gera recibo (SRP violado).

#Se quiser trocar o meio de pagamento (PIX, PayPal, etc.), precisa reescrever a classe (OCP violado).

#Tudo está acoplado diretamente, sem abstrações (DIP ignorado totalmente).

#Nenhuma separação de responsabilidades. Um caos.

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(price for _, price in self.items)


class PaymentProcessor:
    def process_payment(self, order, card_number):
        print(f"Processing payment for R$ {order.calculate_total()} using card {card_number}")
        print("Payment approved")
        print(f"Generating receipt for R$ {order.calculate_total()}")
