class CollinearPoints {
    static boolean areCollinear(Point p1, Point p2, Point p3) {
        double slope1 = (p2.y - p1.y) / (p2.x - p1.x);
        double slope2 = (p3.y - p2.y) / (p3.x - p2.x);

        return Double.compare(slope1, slope2) == 0;
    }
}