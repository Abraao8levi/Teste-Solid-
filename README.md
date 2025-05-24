# Teste Solid 
## Solid em Duas Etapas

### Duas Opções

1. **Código Solid problemático**
2. **Código refatorado**

| Princípio | Aplicação                                                                                 |
|-----------|------------------------------------------------------------------------------------------|
| **SRP**   | `Order` gerencia apenas itens; `CardPayment` apenas pagamentos; `ReceiptGenerator` apenas recibos |
| **OCP**   | Novos métodos de pagamento (ex: `PixPayment`) podem ser adicionados sem alterar código existente |
| **DIP**   | `OrderService` depende de abstrações (`PaymentMethod`, `ReceiptGenerator`)               |
| **ISP**   | Caso `PaymentMethod` cresça demais, pode ser dividido em interfaces menores              |
| **LSP**   | `CardPayment` herda de `PaymentMethod` sem alterar o comportamento esperado              |
