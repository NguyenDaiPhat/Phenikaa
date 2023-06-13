import java.io.*;

public class bai5 {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Nhap ten tep tin: ");
            String fileName = reader.readLine();
            
            FileWriter writer = new FileWriter(fileName);
            
            String line;
            do {
                System.out.print("Nhap mot chuoi (de thoat nhap 'exit'): ");
                line = reader.readLine();
                if (!line.equals("exit")) {
                    String upperCaseLine = line.toUpperCase();
                    writer.write(upperCaseLine);
                    writer.write(System.lineSeparator());
                }
            } while (!line.equals("exit"));
            
            writer.close();
            
            FileReader fileReader = new FileReader(fileName);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            System.out.println("cac chuoi da ghi vao tep tin:");
            String fileLine;
            while ((fileLine = bufferedReader.readLine()) != null) {
                System.out.println(fileLine);
            }
            
            bufferedReader.close();
        } catch (IOException e) {
            System.out.println("Da co loi xay ra: " + e.getMessage());
        }
    }
}