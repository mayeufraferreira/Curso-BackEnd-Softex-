public abstract class Vehicle {

    public String model;
    public String brand;
    public String color;
    public int numWheels;

    public Vehicle() {super();}

    public Vehicle(String model, String brand, String color, int numWheels) {
        super();
        this.model = model;
        this.brand = brand;
        this.color = color;
        this.numWheels = numWheels;
    }

    public String getModel() {
        return getModel();
    }

    public void setModel() {
        this.setModel();
    }

    public String getBrand() {
        return getBrand();
    }

    public void setBrand() {
        this.setBrand();
    }

    public String getColor() {
        return getColor();
    }

    public void setColor() {
        this.setColor();
    }

    public int getNumWheels() {
        return getNumWheels();
    }

    public void setNumWheels() {
        this.setNumWheels();
    }

    public abstract Vehicle clone();


}
