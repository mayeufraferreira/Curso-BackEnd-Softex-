import java.io.*;

public class Ser_Des {

    public static void main (String[] args) throws IOException, ClassNotFoundException {
        Produto produto = new Produto("Notebook", 2265.5d);
        System.out.println(produto);

        //Serialização:
        ObjectOutputStream objectOut = new ObjectOutputStream(new FileOutputStream("produto.byte"));
        objectOut.writeObject(produto);
        objectOut.close();

        //Desserialização:
        ObjectInputStream objectInput = new ObjectInputStream(new FileInputStream("produto.byte"));
        produto = (Produto) objectInput.readObject();
        objectInput.close();
        System.out.println(produto);
    }
}
