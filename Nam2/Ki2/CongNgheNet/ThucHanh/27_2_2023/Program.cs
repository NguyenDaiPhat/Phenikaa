using System;
using System.Collections;
namespace baitap27_2
{
    class Program
    {
        static void Main(string[] argv)
        {
            Teacher teacher = new Teacher();
            Student student = new Student();
            ArrayList arrayList = new ArrayList();
            arrayList.Add(teacher);
            arrayList.Add(student);
        }
    }
}