package org.example;

import java.util.Scanner;

import static java.lang.Math.sqrt;

public class baitap {
    public void ptb1(double a, double b){
        if (a == 0){
            if(b == 0)System.out.println("Phuong trinh vo so nghiem");
            else System.out.println("Phuong trinh vo nghiem");
        }
        else System.out.println("Phuong trinh co 1 nghiem duy nhat la: " + -b/a);
    }
    public void ptb2(double a, double b, double c){
        if (a == 0){
            ptb1(b,c);
        }
        else{
            double delta = b*b-4*a*c;
            if (delta < 0) System.out.println("Phuong trinh vo nghiem");
            else if (delta == 0) System.out.println("Phuong trinh co nghiem kep " + -b/(2*a));
            else System.out.println("Phuong trinh co hai nghiem phan biet " + (-b+sqrt(delta))/(2*a) +" va " + (-b-sqrt(delta))/(2*a));
        }
    }
    public void sapxep(int[] a, int n){
        for(int i = 0;i < n-1; i++)
            for(int j = i+1; j < n; j++){
                if(a[i] > a[j]){
                    int tg = a[i];
                    a[i] = a[j];
                    a[j] = tg;
                }
            }
        System.out.println("Mang sau khi xep tang dan la: ");
        for(int i = 0; i < n; i++){
            System.out.print(a[i]+ " ");
        }
    }
}
