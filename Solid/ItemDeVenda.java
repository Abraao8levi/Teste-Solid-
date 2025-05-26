public class ItemDeVenda {
    private double valor;
    private double quantidade;

    public ItemDeVenda(double valor, double quantidade) {
        this.valor = valor;
        this.quantidade = quantidade;
    }

    public double getValor() {
        return valor;
    }

    public double getQuantidade() {
        return quantidade;
    }

    public double calcularSubtotal() {
        return valor * quantidade;
    }
}
// /*  No código acima, o princípio de Responsabilidade Única foi aplicado, pois a classe ItemDeVenda é responsável
// apenas por manter as informações de um item vendido e calcular o subtotal desse item. A classe Venda pode
// ser refatorada para usar a classe ItemDeVenda, mantendo a responsabilidade de calcular o total da venda. */