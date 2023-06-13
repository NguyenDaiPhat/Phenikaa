package org.example;

class Datee {
    private int n ;

    public void setThang(int n) {
        this.n = n;
    }

    public int getThang() {
        return n;
    }
    Datee (){
    }
    Datee (int getThang){
        this.n = getThang;
    }

    public void xuatNgay(){
        int m;
        switch (n){
            case  1,3,5,7,8,10,12:
                m = 31;
                break;
            case 4, 6,9,11:
                m = 30;
                break;
            case 2:
                m = 29;
                break;
            default:
                m = 0;
                break;
        }
        if(m == 0) System.out.println("khong hop le");
        else{
            if(n == 2) System.out.println("Thang 2 co 28 hoac 29 ngay");
            else System.out.printf("Thang %d co %d ngay", n,m);
        }
    }
}
