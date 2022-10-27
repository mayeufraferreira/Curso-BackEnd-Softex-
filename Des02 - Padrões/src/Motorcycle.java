public class Motorcycle extends Vehicle {

    public String handlebar;

    public Motorcycle(String model, String brand, String color, int numWheels, String handlebar) {
        super(model, brand, color, numWheels);
        this.handlebar = handlebar;
    }

    public String getHandlebar() {
        return getHandlebar();
    }

    public void setHandlebar() {
        this.setHandlebar();
    }

    @Override
    public Vehicle clone() {
        Motorcycle moto = new Motorcycle(this.model,this.brand,this.color,this.numWheels,this.handlebar);
        return moto;
    }

    @Override
    public String toString() {
        return "Moto: [Modelo: " + model + " | " + "Marca: " + brand + " | " +
                "Cor: " + color + " | " + "Número de rodas: " + numWheels + " | "
                + "Guiador/Guidão: " + handlebar + "]";
    }
}
