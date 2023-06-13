public class Line {
    private Point point1;
    private Point point2;
    private double slope;
    private double yIntercept;

    public Line(Point point1, Point point2) {
        this.point1 = point1;
        this.point2 = point2;
        slope = (point2.y - point1.y) / (point2.x - point1.x);
        yIntercept = point1.y - slope * point1.x;
    }
    public String getEquation() {
        return "y = " + slope + "x + " + yIntercept;
    }
}
