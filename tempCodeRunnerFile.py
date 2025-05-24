# Criação do pedido e adição de itens
order = Order()
order.add_item("X-Burger", 25)
order.add_item("Suco", 8)

# Definição do método de pagamento e do gerador de recibo
payment = CardPayment("1234-5678-9012-3456")
receipt = ReceiptGenerator()

# Serviço de processamento do pedido
service = OrderService(payment, receipt)
service.checkout(order)