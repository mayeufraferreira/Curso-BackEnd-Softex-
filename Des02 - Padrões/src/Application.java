
public class Application {

    public static void main(String[] args) {
        Vehicle[] vehicles = new Vehicle[6];
        Car car = new Car("Sedã", "Renault", "Cinza", 4, 4);
        vehicles[0] = car;
        vehicles[1] = car.clone();
        vehicles[2] = car.clone();

        Motorcycle moto = new Motorcycle("CG125", "Honda", "Vermelho", 2, "Honda");
        vehicles[3] = moto;
        vehicles[4] = moto.clone();
        vehicles[5] = moto.clone();

        for (Vehicle vehicle : vehicles) {
            System.out.println(vehicle);
        }

    }
}

/* O método para criar um array que clona os elementos do array já existente não estava funcionando,
quando funcionou não fez o corretamente, então adaptei o código para um jeito que funcionasse e
printasse os elementos na tela */


