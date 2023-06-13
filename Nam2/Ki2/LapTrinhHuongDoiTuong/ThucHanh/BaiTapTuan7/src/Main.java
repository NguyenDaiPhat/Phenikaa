import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //javac -d . AccountBalance.java // tự động tạo package có trong file accoubalan
        Student student = new Student("cc", 11, "vcl");
        student.showInfo();
    }
}