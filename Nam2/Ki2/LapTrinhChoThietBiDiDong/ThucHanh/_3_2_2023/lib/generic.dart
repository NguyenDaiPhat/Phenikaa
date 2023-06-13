class Data<T> {
  T data;
  Data(this.data);
}

double tong<T extends double>(T value, T value2) {
  return value + value2;
}

abstract class Shape {
  double get area;
}

class Circle implements Shape {
  final double radius;
  Circle(this.radius);
  @override
  double get area => 3.14 * radius * radius;
}

class Rectangle implements Shape {
  final double width;
  final double length;

  Rectangle(this.length, this.width);
  @override
  double get area => width * length;
}

class Region<T extends Shape> {
  List<T> shapes;
  Region({required this.shapes});

  double get TotalArea {
    double total = 0;
    shapes.forEach((shape) {
      total += shape.area;
    });
    return total;
  }
}

void main() {
  Data<int> intData = Data<int>(10);
  Data<double> doubleData = Data<double>(10.5);
  Data<String> stringData = Data<String>("Thanh grap");

  print("Int data: ${intData.data}");
  print("String : ${stringData.data}");
  print("Tong : ${tong<double>(1000.2, 200.2)}");
  var circle = Circle(10);
  var retangle = Rectangle(10, 20);
  var rg = Region(shapes: [circle, retangle]);
  print("Total Area of Region : ${rg.TotalArea}");
  print(rg.shapes[0].area);
  print(rg.shapes[1].area);
}
