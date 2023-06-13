import java.io.*;

public class ByteArrayInputStreamExample {
    public static void main(String[] args) {
        byte[] byteArray = new byte[100];
        for (int i = 0; i < byteArray.length; i++) {
            byteArray[i] = (byte) (i + 1);
        }
        try (ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(byteArray)) {
            int i;
            while ((i = byteArrayInputStream.read()) != -1) {
                System.out.print(i + " ");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
