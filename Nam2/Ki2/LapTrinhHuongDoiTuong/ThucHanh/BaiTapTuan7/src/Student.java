public class Student extends Person{
    public Student(String Name, int Age, String Sex){
        super.Name = Name;
        super.Age = Age;
        super.Sex = Sex;
    }
    @Override
    void showInfo() {
        System.out.println("Hello" + super.Name + super.Sex+ Age);
    }
}
