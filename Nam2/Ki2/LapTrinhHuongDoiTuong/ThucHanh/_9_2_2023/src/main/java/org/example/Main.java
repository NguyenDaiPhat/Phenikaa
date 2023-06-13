package org.example;
import java.util.Scanner;
import static java.lang.Math.sqrt;

class Point {
    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double distanceTo(Point other) {
        double dx = other.getX() - x;
        double dy = other.getY() - y;
        return Math.sqrt(dx*dx + dy*dy);
    }
}

class Line {
    private double a;
    private double b;
    private double c;

    public Line(Point p1, Point p2) {
        this.a = p1.getY() - p2.getY();
        this.b = p2.getX() - p1.getX();
        this.c = p1.getX()*p2.getY() - p2.getX()*p1.getY();
    }

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }

    @Override
    public String toString() {
        return a + "x + " + b + "y + " + c + " = 0";
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Nhap toa do diem thu nhat: ");
        double x1 = input.nextDouble();
        double y1 = input.nextDouble();
        Point p1 = new Point(x1, y1);

        System.out.println("Nhap toa do diem thu hai: ");
        double x2 = input.nextDouble();
        double y2 = input.nextDouble();
        Point p2 = new Point(x2, y2);

        Line line = new Line(p1, p2);
        double khoangCach = p1.distanceTo(p2);
        System.out.println("Phuong trinh cua duong thang di qua hai diem: " + line);
        System.out.println("Khoang cach 2 diem la: " + khoangCach);
    }
}
