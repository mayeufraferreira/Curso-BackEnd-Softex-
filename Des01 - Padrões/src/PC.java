
public class PC implements Computer {

    private String type;
    private String RAM;
    private String HDD;
    private String CPU;

    public PC () {}

    public PC (String type, String RAM, String HDD, String CPU) {
        this.type = type;
        this.RAM = RAM;
        this.HDD = HDD;
        this.CPU = CPU;
    }

    public String getType() {
        return type;
    }

    public String getRAM() {
        return RAM;
    }

    public String getHDD() {
        return HDD;
    }

    public String getCPU() {
        return CPU;
    }

    public String getDescription() {
        return type;
    }

    public String toString() {
        return "[Type: " + type + " | " + " RAM: " + RAM + " GB" + " | " + " HD: " + HDD + " GB" + " | " + " CPU: " + CPU + " GHz" + "]";
    }
}



