package org.example;

import java.sql.SQLOutput;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        baitap baitap = new baitap();
        System.out.println("nhap 2 tham so a, b pt ax+b=0");
        Scanner ip = new Scanner(System.in);
        double a = ip.nextDouble();
        double b = ip.nextDouble();
        baitap.ptb1(a,b);
        System.out.println("nhap 3 tham so a, b, c pt ax^2+bx+c=0");
        a = ip.nextDouble();
        b = ip.nextDouble();
        double c = ip.nextDouble();
        baitap.ptb2(a,b,c);
        System.out.println("Nhap so phan tu mang can sap xep: ");
        int n = ip.nextInt();
        int[] arr = new int[n];
        System.out.println("Nhap cac phan tu: ");
        for(int i = 0; i < n ; i++){
            arr[i] = ip.nextInt();
        }
        System.out.println("Mang chua sap xep la: ");
        for(int i = 0; i < n ; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println("");
        baitap.sapxep(arr,n);
    }
}