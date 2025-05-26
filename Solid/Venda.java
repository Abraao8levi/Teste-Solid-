package controller;
import java.util.ArrayList;
import java.util.List;

public class    Venda {
    private List<Double> itemValores = new ArrayList<Double>();
    private List<Double> itemQuantidades = new ArrayList<Double>();
    public double total(){
        double soma =0;
        for (int i = 0; i < itemValores.size(); i++) {
            soma += itemValores.get(i) * itemQuantidades.get(i);
        }
        return soma;
    }
    public void adicionarItem(double valor) {
        itemValores.add(valor);
        itemQuantidades.add(1.0);
    }
    public void adicionarItem(double valor, double quantidade) {
        itemValores.add(valor);
        itemQuantidades.add(quantidade);
    }
}
/*  No código acima, o princípio de Responsabilidade Única não está sendo aplicado, pois as informações dos 
itens vendidos estão sendo mantidos na classe Venda */