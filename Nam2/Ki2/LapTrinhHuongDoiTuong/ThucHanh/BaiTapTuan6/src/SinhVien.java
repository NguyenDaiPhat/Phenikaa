class SinhVien extends Person {

    int masv;
    int sl;
    Monhoc []dsmh;
    double tong;
    static class Monhoc{
        int Mamh;
        String tenmh;
        double diemgk,diemck;
        public Monhoc(String tenmh, int Mamh, double diemgk, double diemck ){
            this.tenmh=tenmh;
            this.Mamh=Mamh;
            this.diemgk=diemgk;
            this.diemck=diemck;
        }
        public void setTenMH(String tenmh){
            this.tenmh=tenmh;
        }
        public void setmaMH(int mamh){
            this.Mamh=mamh;
        }
        public void setDiemgk(double diemgk){
            this.diemgk=diemgk;
        }
        public void setDiemck(double diemck){


            this.diemck=diemck;
        }
        public String getTenmh(){
            return this.tenmh;
        }
        public int getmaMH(){
            return this.Mamh;
        }
        public double getDiemgk(){
            return this.diemgk;
        }
        public double getDiemck(){
            return this.diemck;
        }
    }
    public SinhVien(String ten, int tuoi, int maSV, int sl) {
        super(ten,tuoi);
        this.masv = maSV;
        this.sl=sl;
    }
    SinhVien(String ten) {
        super(ten);
    }
    SinhVien(int tuoi) {
        super(tuoi);
    }
    SinhVien(SinhVien a){
        super(a);
        this.masv=a.masv;
        this.sl=a.sl;
        this.dsmh=a.dsmh;
        this.tong=a.tong;
    }
    public void setdsmh(Monhoc []dsmh){
        this.dsmh=dsmh;
    }


    public String getTen(){
        return this.tensv;
    }
    public int getmssv(){
        return this.masv;
    }
    public Monhoc[] getdsmh(){
        return this.dsmh;
    }
    public void xuattenmh(){

        for (int i=0;i<sl;i++){
            System.out.print(dsmh[i].getTenmh()+" ");
        }
    }
    public double getdiemtb(){

        for (int i=0;i<sl;i++){
            this.tong+=dsmh[i].diemgk;
            this.tong+=dsmh[i].diemck;
        }
        this.tong/=(2*sl);
        return this.tong;
    }

}

