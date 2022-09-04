import java.io.Serial;
import java.io.Serializable;

public class Produto implements Serializable {

    private String nome;
    private Double preco;

    public Produto() {}

    public Produto(String nome, Double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(){
        this.nome = nome;
    }

    public Double getPreco() {
        return preco;
    }

    public void setPreco() {
        this.preco = preco;
    }

    @Override
    public String toString(){
        return "Produto [" + "Nome: " + nome + " | " + "Preço: R$" + preco + "]";
    }
}
