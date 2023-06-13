import 'package:dart2_2_2023/dart2_2_2023.dart' as dart2_2_2023;

class SinhVien {
  var msv;
  var ten;
  var sex;
  SinhVien() {}

  SinhVien.khoitao(String msv, String ten, bool sex) {
    this.msv = msv;
    this.ten = ten;
    this.sex = sex;
  }

  void hienThiThongTin() {
    var gioitin;
    gioitinh == true || sex == true ? gioitin = "nam" : gioitin = "nu";
    print("ma sinh vien: ${msv}, ten: ${ten}, sex ${gioitin}");
  }

  set masinhvien(String msv) {
    this.msv = msv;
  }

  String get masinhvien {
    return msv;
  }

  set hovaten(String ten) {
    this.ten = ten;
  }

  String get hovaten {
    return ten;
  }

  set gioitinh(bool sex) {
    this.sex = sex;
  }

  bool get gioitinh {
    return sex;
  }
}

class sinhVienDaiCuong extends SinhVien {
  // var diemDaiCuong;
  // set diemSinhVienDaiCuong(var diemDaiCuong) {
  //   this.diemDaiCuong = diemDaiCuong;
  // }
  // int get diemSinhVienDaiCuong{
  //   return diemDaiCuong;
  // }
}

// class siv extends SinhVien {}

abstract class Hinh {
  double getChuVi();
  double getDienTich();
  void hienthi() {
    print("chu vi: ${getChuVi()}, dien tich: ${getDienTich()}");
  }
}

class HinhTron extends Hinh {
  var bankinh;
  HinhTron() {}
  HinhTron.khoitao(double bankinh) {
    this.bankinh = bankinh;
  }
  set bk(var bankinh) {
    this.bankinh = bankinh;
  }

  double get bk {
    return bankinh;
  }

  @override
  getChuVi() {
    // TODO: implement getChuVi

    return bankinh * 2 * 3.14;
  }

  @override
  getDienTich() {
    // TODO: implement getDienTich
    return bankinh * bankinh * 3.14;
  }
}

class HinhChuNhat extends Hinh {
  var chieudai, chieurong;
  set cd(double chieudai) {
    this.chieudai = chieudai;
  }

  double get cd {
    return chieudai;
  }

  set cr(double chieurong) {
    this.chieurong = chieurong;
  }

  double get cr {
    return chieurong;
  }

  @override
  getChuVi() {
    // TODO: implement getChuVi

    return (chieudai + chieurong) * 2;
  }

  @override
  getDienTich() {
    // TODO: implement getDienTich
    return chieudai * chieurong;
  }
}

void main() {
  // var sv = SinhVien.khoitao("Nguyen Dai", 1);
  var sv1 = SinhVien();
  sv1.gioitinh = false;
  sv1.hienThiThongTin();

  // sv.name = " Nguyen Dai Phat";
  // // sv.hoTen = "Ng";
  // sv.tuoi = 19;
  // HinhTron ht = HinhTron();
  // HinhTron htt = HinhTron.khoitao(3);
  // ht.bk = 2;
  // // ht.bankinh = 1;
  // ht.hienthi();
  // Hinh htt = HinhChuNhat();
}
