public class Factory {

    public static Computer createComputer(String type) {
        if (type == "PC") {
            return new PC();
        } else if (type == "Server") {
            return new Server();
        }
        return null;
    }
}

