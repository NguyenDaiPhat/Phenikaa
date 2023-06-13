import static java.lang.Integer.parseInt;

public class Main {
    public static void main(String[] args) {
        int[] Mang = new int[args.length];
        for(int i = 0; i < args.length; i++) {
            Mang[i] = parseInt(args[i]);
        }
        System.out.println("Day khi chua sap xep la:");
        for (int i: Mang) {
            System.out.print(i+" ");
        }
        System.out.println();
        Quicksort quickSort = new Quicksort();
        quickSort.quickSort(Mang, 0 , Mang.length - 1);
        System.out.println("Day sau khi sap xep la:");
        for (int i: Mang) {
            System.out.print(i+" ");
        }
    }
}