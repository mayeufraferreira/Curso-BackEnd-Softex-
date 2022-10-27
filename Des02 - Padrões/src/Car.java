public class Car extends Vehicle {

    public int numDoor;

    public Car(String model, String brand, String color, int numWheels, int numDoor) {
        super(model, brand, color, numWheels);
        this.numDoor = numDoor;
    }

    public int getNumDoor() {
        return getNumDoor();
    }

    public void setNumDoor() {
        this.setNumDoor();
    }

    @Override
    public Vehicle clone() {
        Car car = new Car(this.model,this.brand,this.color,this.numWheels,this.numDoor);
        return car;
    }

    @Override
    public String toString() {
        return "Carro: [Modelo: " + model + " | " + "Marca: " + brand + " | " +
                "Cor: " + color + " | " + "Número de rodas: " + numWheels + " | "
                + "Número de portas: " + numDoor + "]";
    }
}