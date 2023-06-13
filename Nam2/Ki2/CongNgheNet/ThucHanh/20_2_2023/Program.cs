// Viết chương trình C# có ba lớp: Person, Student (:Person), Teacher (: Person).
// • Lớp Person: hai phương thức Hello () và SetAge (int age) gán tuổi của người đó.
// • Lớp Student: phương thức Study() hiển thị ra màn hình “I’m studying”; ShowAge () hiển thị “My age is: x year old”.
// • Lớp Teacher: phương thức Teach() hiển thị ra màn hình “I’m teaching”.
// Phương thức Main thực hiện những việc sau:
// • Tạo một Người mới và giúp anh ấy nói lời chào
// • Tạo Sinh viên mới, đặt tuổi, chào và hiển thị tuổi của SV trên màn hình.
// • Tạo Giáo viên mới, đặt tuổi, chào và bắt đầu giảng dạy.

using System;
namespace BaiThucHanh5{
    class Program{
        static void Main(){
            Person person = new Person();
            person.Hello();
            Student student = new Student();
            student.SetAge(20);
            student.Hello();
            student.ShowAge();
            Teacher teacher = new Teacher();
            teacher.SetAge(30);
            teacher.Hello();
            teacher.Teach();
        }
    }
}