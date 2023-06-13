using System;
namespace HelloWorld
{
    class Bai1
    {
        public void tamgiaccan()
        {
            Console.WriteLine("Nhap 3 canh tam giac tren 3 dong:");
            float a, b, c;
            a = float.Parse(Console.ReadLine());
            b = float.Parse(Console.ReadLine());
            c = float.Parse(Console.ReadLine());
            if ((a + b <= c) || (a + c <= b) || (b + c <= a))
            {
                Console.WriteLine("a, b, c khong phai 3 canh tam giac");
            }
            else
            {
                if (a == b || b == c || c == a)
                {
                    Console.WriteLine("a, b, c la 3 canh tam giac can");
                }
                else
                {
                    Console.WriteLine("a, b, c khong phai 3 canh tam giac can");
                }
            }
        }
    }
}