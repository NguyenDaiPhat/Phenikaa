import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String host = "localhost"; 
        int port = 2023; 
        //String input = "Xin chao Viet Hoang ! Ban khoe chu"; 
        
        try {
           
            Socket socket = new Socket(host, port);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("nhap vao du lieu can gui : ");
            String input = br.readLine();

            
            System.out.println("Client input: " + input);
            out.println(input);

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String output = in.readLine();
            // System.out.println("Client nhan: " + output);
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
