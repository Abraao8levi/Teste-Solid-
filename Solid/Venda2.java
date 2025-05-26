import java.util.ArrayList;
import java.util.List;
import model.ItemDeVenda;
import model.Venda2;

public class Venda2 {
    private List<ItemDeVenda> itens = new ArrayList<>();

    public void adicionarItem(double valor, double quantidade) {
        ItemDeVenda item = new ItemDeVenda(valor, quantidade);
        itens.add(item);
    }

    public double total() {
        double soma = 0;
        for (ItemDeVenda item : itens) {
            soma += item.calcularSubtotal();
        }
        return soma;
    }
    public void adicionarItem(double valor) {
        adicionarItem(valor, 1.0);
    }
}