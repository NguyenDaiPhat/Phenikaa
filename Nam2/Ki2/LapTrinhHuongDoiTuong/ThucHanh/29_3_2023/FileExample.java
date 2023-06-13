import java.io.*;

public class FileExample {
    public static void main(String[] args) {
        String fileName = "example.txt"; 
        String content = "Lop thuc hanh Oop sang thu 4"; 
        try {
            FileOutputStream hoang = new FileOutputStream(fileName);
            hoang.write(content.getBytes()); 
            hoang.close(); 
            
            FileInputStream hoang1 = new FileInputStream(fileName);
            byte[] a = new byte[1024];
            int bytesRead = hoang1.read(a); 
            hoang1.close(); 
            
            String readContent = new String(a, 0, bytesRead);
            System.out.println(readContent);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
