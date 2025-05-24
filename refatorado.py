


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(price for _, price in self.items)

class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Implement in subclass")

class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Processing card payment of R$ {amount} using card {self.card_number}")
        print("Payment approved")


class ReceiptGenerator:
    def generate(self, amount):
        print(f"Generating receipt for R$ {amount}")

class OrderService:
    def __init__(self, payment_method: PaymentMethod, receipt_generator: ReceiptGenerator):
        self.payment_method = payment_method
        self.receipt_generator = receipt_generator

    def checkout(self, order: Order):
        total = order.calculate_total()
        self.payment_method.pay(total)
        self.receipt_generator.generate(total)

# código de teste
order = Order()
order.add_item("X-Burger", 25)
order.add_item("Suco", 8)

payment = CardPayment("1234-5678-9012-3456")
receipt = ReceiptGenerator()

service = OrderService(payment, receipt)
service.checkout(order)