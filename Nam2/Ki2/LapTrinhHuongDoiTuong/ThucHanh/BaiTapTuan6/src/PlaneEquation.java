class PlaneEquation {
    static void getPlaneEquation(Point3D p1, Point3D p2, Point3D p3) {
        double a = (p2.y - p1.y) * (p3.z - p1.z) - (p2.z - p1.z) * (p3.y - p1.y);
        double b = (p2.z - p1.z) * (p3.x - p1.x) - (p2.x - p1.x) * (p3.z - p1.z);
        double c = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);
        double d = -(a * p1.x + b * p1.y + c * p1.z);

        System.out.println("Phương trình mặt phẳng đi qua 3 điểm: " + a + "x + " + b + "y + " + c + "z + " + d + " = 0");
    }
}