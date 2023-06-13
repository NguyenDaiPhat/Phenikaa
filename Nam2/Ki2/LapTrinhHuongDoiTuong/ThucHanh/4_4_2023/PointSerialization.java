import java.io.*;

class Point implements Serializable {
    private static final long serialVersionUID = 1L;
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

public class PointSerialization {
    public static void main(String[] args) {
        Point p1 = new Point(10, 20);
        Point p2 = new Point(30, 40);

        try (FileOutputStream fos = new FileOutputStream("points.txt");
                ObjectOutputStream oos = new ObjectOutputStream(fos);) {
            oos.writeObject(p1);
            oos.writeObject(p2);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (FileInputStream fis = new FileInputStream("points.txt");
                ObjectInputStream ois = new ObjectInputStream(fis);) {
            Point p1Deserialized = (Point) ois.readObject();
            Point p2Deserialized = (Point) ois.readObject();
            System.out.println("p1: (" + p1Deserialized.getX() + ", " + p1Deserialized.getY() + ")");
            System.out.println("p2: (" + p2Deserialized.getX() + ", " + p2Deserialized.getY() + ")");
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
