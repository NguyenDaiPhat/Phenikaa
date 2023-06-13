import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 2023; 
        try {
   
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server dang chay va lang nghe ket noi tu Client...");
            
            while (true) {
       
                Socket socket = serverSocket.accept();
                
                
                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                
         
                String input = br.readLine();
                System.out.println("Nhan du lieu tu Client: " + input);
                
                
                String output = input.toUpperCase();
                
                
                PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
                
                
                pw.println(output);
                
                
                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
