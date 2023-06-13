import java.io.*;
import java.util.*;

public class StudentList implements Serializable {
    private static final long serialVersionUID = 1L;
    private List<Student> students;

    public StudentList() {
        students = new ArrayList<>();
    }

    public void addStudent(Student s) {
        students.add(s);
    }

    public void sort() {
        Collections.sort(students, new Comparator<Student>() {
            public int compare(Student s1, Student s2) {
                return Double.compare(s1.getAverageScore(), s2.getAverageScore());
            }
        });
    }

    public void print() {
        for (Student s : students) {
            System.out.println(s.toString());
        }
    }

    public static void main(String[] args) {
        StudentList list = new StudentList();
        list.addStudent(new Student("John", 7.5, 8.5, 9.0));
        list.addStudent(new Student("Mary", 8.0, 7.5, 8.5));
        list.addStudent(new Student("Peter", 9.0, 8.5, 9.5));

        //ghi danh sach sinh vien vao tep student.ser
        try (FileOutputStream fos = new FileOutputStream("students.ser");
             ObjectOutputStream oos = new ObjectOutputStream(fos);) {
            oos.writeObject(list);
        } catch (IOException e) {
            e.printStackTrace();
        }

        //doc lai danh sach sinh vien tu students.ser

        try (FileInputStream fis = new FileInputStream("students.ser");
             ObjectInputStream ois = new ObjectInputStream(fis);) {
            StudentList listDeserialized = (StudentList) ois.readObject();

            //sap xep danh sach sinh vien theo diem trung binh tang dan
            listDeserialized.sort();

            // ghi danh sach sinh vien da sap xep vao tep sxsv.dat
            try (FileOutputStream fos = new FileOutputStream("sxsv.dat");
                 ObjectOutputStream oos = new ObjectOutputStream(fos);) {
                oos.writeObject(listDeserialized);
            } catch (IOException e) {
                e.printStackTrace();
            }

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}

class Student implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private double mathScore;
    private double literatureScore;
    private double englishScore;

    public Student(String name, double mathScore, double literatureScore, double englishScore) {
        this.name = name;
        this.mathScore = mathScore;
        this.literatureScore = literatureScore;
        this.englishScore = englishScore;
    }

    public String getName() {
        return name;
    }

    public double getMathScore() {
        return mathScore;
    }

    public double getLiteratureScore() {
        return literatureScore;
    }

    public double getEnglishScore() {
        return englishScore;
    }

    public double getAverageScore() {
        return (mathScore + literatureScore + englishScore) / 3;
    }

    @Override
    public String toString() {
        return name + ": " + getAverageScore();
    }
}
