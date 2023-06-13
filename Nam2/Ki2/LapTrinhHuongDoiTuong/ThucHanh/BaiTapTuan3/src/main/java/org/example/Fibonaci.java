package org.example;

import java.util.Scanner;

public class Fibonaci {
    private int n ;

    public void setNumberFibo(int n) {
        this.n = n;
    }

    public int getNumberFibo() {
        return n;
    }
    Fibonaci (){
    }
    Fibonaci (int getNumberFibo){
        this.n = getNumberFibo;
    }

    public void xuatFibo(){
        int fi1 = 1, fi2 = 1, fi3;
        System.out.println("Day n so fibonaci la: ");
        if(n <=0) {
            System.out.println("Khong hop le");
            return ;
        }
        if(n == 1) {System.out.print(fi1+ " ");return ;}
        else if( n== 2) {System.out.print(fi1 + " " + fi2 + " "); return ;}
        else {
            System.out.print(fi1 + " " + fi2 + " ");
            while (n-2!= 0){
                fi3  = fi1 + fi2;
                fi1 = fi2;
                fi2 = fi3;
                n--;
                System.out.print(fi3 + " ");
            }
        }

        System.out.println();
    }
}
