import java.io.*;

public class ByteArrayOutputExample {
    public static void main(String[] args) {
        byte[] arr = new byte[100]; 
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (byte) i; 
        }

        
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        try {
            outputStream.write(arr); 
        } catch (IOException e) {
            e.printStackTrace();
        }

        
        byte[] arr2 = outputStream.toByteArray();
        System.out.println("Mang byte dich:");
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(arr2[i] + " ");
        }
    }
}
