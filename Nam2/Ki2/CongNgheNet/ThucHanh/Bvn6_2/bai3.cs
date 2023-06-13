using System;
namespace HelloWorld
{
    class Bai3
    {
        public void PhuongTrinhBacHai()
        {
            Console.WriteLine("Nhap a, b, c ptbh tren 3 dong ");
            float a, b, c;

            a = float.Parse(Console.ReadLine());
            b = float.Parse(Console.ReadLine());
            c = float.Parse(Console.ReadLine());
            if (a == 0)
            {
                if (b == 0)
                {
                    if (c == 0)
                    {
                        Console.WriteLine("Phuong trinh vo so nghiem");
                    }
                    else
                    {
                        Console.WriteLine("Phuong trinh vo nghiem");
                    }
                }
                else
                {
                    Console.WriteLine($"Phuong trinh co 1 nghiem: {-b / a}");
                }

            }
            else
            {
                float delta = b * b - 4 * a * c;
                if (delta == 0)
                {
                    Console.WriteLine($"Phuong trinh co 1 nghiem: {-b / (2 * a)}");
                }
                else if (delta < 0)
                {
                    Console.WriteLine("Phuong trinh vo nghiem");
                }
                else
                {
                    Console.WriteLine($"Phuong trinh co 2 nghiem: {(-b + Math.Sqrt(delta)) / (2 * a)} {(-b - Math.Sqrt(delta)) / (2 * a)}");
                }
            }
        }
    }
}