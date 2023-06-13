import java.util.HashMap;
import java.util.Map;
class SanPham {
    public String maSanPham;
    public String tenSanPham;
    public String moTa;
    public String thongTinChiTiet;
    public Map<String, Double> tuyChon;

    public SanPham(String maSanPham, String tenSanPham, String moTa, String thongTinChiTiet) {
        this.maSanPham = maSanPham;
        this.tenSanPham = tenSanPham;
        this.moTa = moTa;
        this.thongTinChiTiet = thongTinChiTiet;
        this.tuyChon = new HashMap<>();
    }

    public void nhapThongTinSanPham(String maSanPham, String tenSanPham, String moTa, String thongTinChiTiet) {
        this.maSanPham = maSanPham;
        this.tenSanPham = tenSanPham;
        this.moTa = moTa;
        this.thongTinChiTiet = thongTinChiTiet;
    }

    public void themTuyChon(String tenTuyChon, double giaTuyChon) {
        tuyChon.put(tenTuyChon, giaTuyChon);
    }

    public void suaTuyChon(String tenTuyChon, double giaTuyChon) {
        if (tuyChon.containsKey(tenTuyChon)) {
            tuyChon.put(tenTuyChon, giaTuyChon);
        } else {
            System.out.println("Không tìm thấy tùy chọn để sửa.");
        }
    }

    public void inThongTinSanPham() {
        System.out.println("Mã sản phẩm: " + maSanPham);
        System.out.println("Tên sản phẩm: " + tenSanPham);
        System.out.println("Mô tả: " + moTa);
        System.out.println("Thông tin chi tiết: " + thongTinChiTiet);
        System.out.println("Danh sách các tùy chọn và giá của sản phẩm:");
        for (Map.Entry<String, Double> entry : tuyChon.entrySet()) {
            System.out.println("- " + entry.getKey() + ": " + entry.getValue());
        }
    }
}
