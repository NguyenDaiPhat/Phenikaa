import java.net.*;

public class PortScanner {
    public static void main(String[] args) {
        String host = "localhost"; 
        int minPort = 0; 
        int maxPort = 1024; 

        System.out.println("Scanning ports on " + host);

        for (int port = minPort; port <= maxPort; port++) {
            try {
                ServerSocket serverSocket = new ServerSocket(port);
                serverSocket.close();
            } catch (Exception ex) {
                System.out.println("Port " + port + " is open");
            }
        }
    }
}