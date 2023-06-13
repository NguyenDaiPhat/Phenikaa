import java.util.Arrays;

public class Args {
    public static void main(String[] args) {
        // kiem tra xem du tham so chua
        if (args.length == 0) {
            System.out.println("Khong co tham so dau vao.");
            return;
        }

        // tao mot mang so thuc de luu tru cac so
        double[] numbers = new double[args.length];

        // chuyen doi cac tham so tu dang chuoi sang dang so thuc
        for (int i = 0; i < args.length; i++) {
            try {
                numbers[i] = Double.parseDouble(args[i]);
            } catch (NumberFormatException e) {
                System.out.println("Tham so khong hop le: " + args[i]);
                return;
            }
        }

        // hien thi day so da nhap
        System.out.println("Day so da nhap:");
        System.out.println(Arrays.toString(numbers));

        // sap xep day so
        Arrays.sort(numbers);

        // hien thi day so da sap xep
        System.out.println("Day so da sap xep:");
        System.out.println(Arrays.toString(numbers));

        // tinh trung binh cong cua day so
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        double average = sum / numbers.length;

        // hien thi trung binh cong
        System.out.printf("Trung binh cong cua day so: %.2f", average);
    }
}