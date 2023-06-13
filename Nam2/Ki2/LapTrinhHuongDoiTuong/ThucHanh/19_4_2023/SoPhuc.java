public class SoPhuc {
    private double thuc;
    private double ao;
    public SoPhuc(){}
    public SoPhuc(double thuc, double ao) {
        this.thuc = thuc;
        this.ao = ao;
    }
    public SoPhuc(SoPhuc t){
        this.thuc = t.getThuc();
        this.ao = t.getAo();
    }
    public void setThuc(double thuc){
        this.thuc = thuc;
    }
    public double getThuc() {
        return thuc;
    }
    public void setAo(double ao){
        this.ao = ao;
    }
    public double getAo() {
        return ao;
    }

    public SoPhuc add(SoPhuc b) {
        double thuc = this.thuc + b.getThuc();
        double ao = this.ao + b.getAo();
        return new SoPhuc(thuc, ao);
    }

    public SoPhuc sub(SoPhuc b) {
        double thuc = this.thuc - b.getThuc();
        double ao = this.ao - b.getAo();
        return new SoPhuc(thuc, ao);
    }

    public SoPhuc mul(SoPhuc b) {
        double thuc = this.thuc * b.getThuc() - this.ao * b.getAo();
        double ao = this.thuc * b.getAo() + this.ao * b.getThuc();
        return new SoPhuc(thuc, ao);
    }

    public SoPhuc div(SoPhuc b) {
        double thuc = (this.thuc * b.getThuc() + this.ao * b.getAo()) / (b.getThuc() * b.getThuc() + b.getAo() * b.getAo());
        double ao = (this.ao * b.getThuc() - this.thuc * b.getAo()) / (b.getThuc() * b.getThuc() + b.getAo() * b.getAo());
        return new SoPhuc(thuc, ao);
    }

    public String toString() {
        if (ao < 0) {
            return thuc + " - " + (-ao) + "i";
        } else {
            return thuc + " + " + ao + "i";
        }
    }
    public static void main(String[] args){
        SoPhuc a = new SoPhuc();
        SoPhuc b = new SoPhuc();
        a.setThuc(1);a.setAo(2);
        b.setThuc(3);b.setAo(4);
        SoPhuc tong = a.add(b);
        SoPhuc hieu = a.sub(b);
        SoPhuc tich = a.mul(b);
        SoPhuc thuong = a.div(b);

        System.out.println("Tong " + tong.toString());
        System.out.println("Hieu: " + hieu.toString());
        System.out.println("Tich: " + tich.toString());
        System.out.println("Thuong: " + thuong.toString());
    }
}