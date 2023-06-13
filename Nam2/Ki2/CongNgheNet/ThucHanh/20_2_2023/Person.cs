using System;
namespace BaiThucHanh5
{
    class Person
    {
        public int age;
        public void Hello()
        {
            System.Console.WriteLine("Hello everyone");
        }
        public void SetAge(int age){
            this.age = age;
        }
    }
}