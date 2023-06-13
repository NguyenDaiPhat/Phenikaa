import java.io.IOException;
import java.io.RandomAccessFile;

public class randomFile {
    public static void main(String[] args) {
        try {
            // Tao tep ngau nhien 
            RandomAccessFile file = new RandomAccessFile("dayso.dat", "rw");

            // ghi mot day so nguyen vao tep
            for (int i = 1; i <= 10; i++) {
                file.writeInt(i);
            }

            // dong tep
            file.close();

            // mo tep de doc day so
            file = new RandomAccessFile("dayso.dat", "r");

            // hien thi day so 
            System.out.println("Day so trong tep tin:");
            while (file.getFilePointer() < file.length()) {
                System.out.println(file.readInt());
            }

            //dong tep
            file.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
