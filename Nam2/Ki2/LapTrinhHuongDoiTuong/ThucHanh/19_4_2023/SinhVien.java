// Bài 2: Tạo lập lớp SinhVien có các thuộc tính
// MaSV
// TenSV
// Diem
// a)Tạo lập các cấu tử
// b) Các phương thức set và get
// c) Tạo lập một mảng danh sách các sinh viên, sắp xếp sinh viên theo thứ tự điểm giảm dần
public class SinhVien {
    private String maSV;
    private String tenSV;
    private double diem;

    public SinhVien(){}
    public SinhVien(String maSV, String tenSV, double diem) {
        this.maSV = maSV;
        this.tenSV = tenSV;
        this.diem = diem;
    }

    public String getMaSV() {
        return maSV;
    }

    public void setMaSV(String maSV) {
        this.maSV = maSV;
    }

    public String getTenSV() {
        return tenSV;
    }

    public void setTenSV(String tenSV) {
        this.tenSV = tenSV;
    }

    public double getDiem() {
        return diem;
    }

    public void setDiem(double diem) {
        this.diem = diem;
    }

    public static void sort(SinhVien[] dsSinhVien) {
        int n = dsSinhVien.length;
        for(int i = 0; i< n-1; i++)
        for(int j =i+1; j<n;j++){
            if(dsSinhVien[i].diem<dsSinhVien[j].diem){
                SinhVien tg = dsSinhVien[i];
                dsSinhVien[i] = dsSinhVien[j];
                dsSinhVien[j] = tg;
            }
        }
    }

    public static void main(String[] args) {
        SinhVien[] dsSinhVien = new SinhVien[4];
        dsSinhVien[0] = new SinhVien("21010625", "Nguyen Dai Phat", 10);
        dsSinhVien[1] = new SinhVien("21010626", "Ngu the", 7.5);
        dsSinhVien[2] = new SinhVien("21010627", "Dep zai khong sai", 9.0);
        dsSinhVien[3] = new SinhVien("21010628", "hihi", 6.5);
        sort(dsSinhVien);
        System.out.println("Danh sach sinh vien sau khi sap xep theo thu tu diem giam dan: ");
        for (SinhVien sv : dsSinhVien) {
            System.out.println(sv.getMaSV() + " " + sv.getTenSV() + " " + sv.getDiem());
        }
    }
}