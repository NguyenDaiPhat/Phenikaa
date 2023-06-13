import 'package:flutter/material.dart';
import 'SinhVien.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  final List<SinhVien> danhSachSinhVien = [
    SinhVien(ma: '2345678',
        hoVaTen: 'Nguyen Quynh Nga',
        ngaySinh: DateTime(2003, 12, 02),
        diemTotNghiep: 7.8),
    SinhVien(ma: '3336688',
        hoVaTen: 'Tran Van Quang',
        ngaySinh: DateTime(2002, 06, 27),
        diemTotNghiep: 8.5),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Flutter App'),
      ),
      body: Column(
        children: <Widget>[
          SizedBox(
            width: double.infinity,
            child: Card(
              color: Colors.blue,
              elevation: 5,
              child: Text('CHART'),
            ),
          ),
          Card(
            children: [
              Card(
                
              )
            ]


          ),
          Column(
            children: [
              Card(
                child: Row(
                  children: <Widget>[
                    Container(
                      margin: EdgeInsets.symmetric(
                        vertical: 10,
                        horizontal: 15,
                      ),
                      decoration: BoxDecoration(
                        border: Border.all(
                          color: Colors.purple,
                          width: 2,
                        ),
                      ),
                      padding: EdgeInsets.all(10),
                      child: Text(
                        danhSachSinhVien[0].diemTotNghiep.toString(),
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 20,
                          color: Colors.purple,
                        ),
                      ),
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Text(
                          danhSachSinhVien[0].ma + ' - ' + danhSachSinhVien[0].hoVaTen,
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        Text(
                          danhSachSinhVien[0].ngaySinh.toString(),
                          style: TextStyle(
                            color: Colors.grey,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
