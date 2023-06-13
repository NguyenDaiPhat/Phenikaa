import java.util.Scanner;

class LCM {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Nhập vào số thứ nhất: ");
        int a = input.nextInt();
        System.out.print("Nhập vào số thứ hai: ");
        int b = input.nextInt();
        int gcd = findGCD(a, b);
        int lcm = (a * b) / gcd;
        System.out.println("Bội chung nhỏ nhất của " + a + " và " + b + " là " + lcm);
    }
    public static int findGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
