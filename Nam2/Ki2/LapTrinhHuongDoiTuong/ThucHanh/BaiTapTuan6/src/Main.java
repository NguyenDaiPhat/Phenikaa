import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Lap phuong trinh duong thang di qua 2 diem
        Point point1 = new Point(1, 2);
        Point point2 = new Point(3, 4);
        Line line = new Line(point1, point2);
        System.out.println("Phương trình của đường thẳng đi qua hai điểm (" + point1.x + ", " + point1.y + ") và (" + point2.x + ", " + point2.y + ") là " + line.getEquation());
        // Lap phuong trinh mat phang di qua 3 diem
        Point3D A = new Point3D(1, 2, 3);
        Point3D B = new Point3D(2, 2, 0);
        Point3D C = new Point3D(3, 1, 1);
        PlaneEquation.getPlaneEquation(A, B, C);
        // Kiem tra 3 diem thang hang
        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
        Point p3 = new Point(5, 6);
        boolean result = CollinearPoints.areCollinear(p1, p2, p3);
        if (result) {
            System.out.println("Ba điểm (" + p1.x + "," + p1.y + ") (" + p2.x + "," + p2.y + ") (" + p3.x + "," + p3.y + ") thẳng hàng");
        } else {
            System.out.println("Ba điểm (" + p1.x + "," + p1.y + ") (" + p2.x + "," + p2.y + ") (" + p3.x + "," + p3.y + ") không thẳng hàng");
        }
        // kiem tra 1 diem co thuoc duong thang hay khong
        Point line1 = new Point(1, 2);
        Point line2 = new Point(3, 4);
        Point p = new Point(5, 7);
        boolean check = CollinearPoints.areCollinear(line1, line2, p);
        if (check) {
            System.out.println("Điểm (" + p.x + "," + p.y + ") thuộc đường thẳng");
        } else {
            System.out.println("Điểm (" + p.x + "," + p.y + ") không thuộc đường thẳng");
        }
        // kiem tra duong thang co cat mat phang hay khong

        //Cai tien person
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap so luong sinh vien: ");
        n=sc.nextInt();

        SinhVien a[]=new SinhVien[n];
        for (int i=0;i<n;i++){
            System.out.print("Nhap ten sinh vien thu "+(i+1)+": ");
            String ten=sc.next();
            System.out.print("Nhap tuoi sinh vien thu "+(i+1)+": ");
            int tuoi=sc.nextInt();
            System.out.print("Nhap mssv thu "+(i+1)+": ");
            int ms=sc.nextInt();
            System.out.print("Nhap so luong mon hoc cua sinh vien thu "+(i+1)+": ");
            int sl=sc.nextInt();
            a [i]=new SinhVien(ten,tuoi,ms,sl);
            SinhVien.Monhoc [] b =new SinhVien.Monhoc[sl];
            for (int j=0;j<sl;j++){
                System.out.print("Nhap ten monhoc thu "+(j+1)+": ");
                String tenmh=sc.next();
                System.out.print("Nhap ma mon hoc thu "+(j+1)+": ");
                int mamh=sc.nextInt();
                System.out.print("Nhap diem giua ky mon hoc cua sinh vien thu "+(i+1)+": ");
                Double dgk=sc.nextDouble();
                System.out.print("Nhap diem cuoi ky mon hoc cua sinh vien thu "+(i+1)+": ");
                Double dck=sc.nextDouble();
                b[j]=new SinhVien.Monhoc(tenmh,mamh,dgk,dck);
                System.out.println();
            }
            a[i].setdsmh(b);
            System.out.println();
        }

        for (int i=0;i<n;i++){
            System.out.print(a[i].getTen()+" "+a[i].masv+" ");
            a[i].xuattenmh();
            System.out.print(a[i].getdiemtb());

            System.out.println();
        }
    }
}
