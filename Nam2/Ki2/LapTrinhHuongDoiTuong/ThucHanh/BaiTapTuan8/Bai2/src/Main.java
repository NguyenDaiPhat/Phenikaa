import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Nhập vào mảng các số
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập số phần tử của mảng: ");
        int n = sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            System.out.printf("Nhập phần tử thứ %d: ", i + 1);
            array[i] = sc.nextInt();
        }
        System.out.println("Các số lẻ trong mảng là:");
        for (int num : array) {
            if (num % 2 != 0) {
                System.out.println(num);
            }
        }
    }
}
