package org.example;

import java.util.Date;
import java.util.Scanner;

public class Main {
    static Boolean checkSnt(int n){
        if(n<2) return false;
        for(int i = 2; i < Math.sqrt(n); i++){
            if(n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        //fibo
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap so luong fibonaci can in: ");
        int soLuongFibo = sc.nextInt();
        Fibonaci fibonaci = new Fibonaci(soLuongFibo);
        fibonaci.xuatFibo();
        //thang ngay
        System.out.print("Nhap thang can in ra ngay: ");
        int thang = sc.nextInt();
        Datee date = new Datee(thang);
        date.xuatNgay();
        //kiem tra snt
        System.out.print("Nhap so n: ");
        int number = sc.nextInt();
        if(checkSnt(number)) System.out.println("n la snt");
        else System.out.println("n khong phai snt");
    }
}