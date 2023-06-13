using System;
namespace HelloWorld
{
    class Bai2
    {
        public void PhuongTrinhBacNhat()
        {
            Console.WriteLine("Nhap a, b ptbn tren 2 dong ");
            float a, b;
            a = float.Parse(Console.ReadLine());
            b = float.Parse(Console.ReadLine());
            if (a == 0)
            {
                if (b == 0)
                {
                    Console.WriteLine("Phuong trinh vo so nghiem");
                }
                else
                {
                    Console.WriteLine("Phuong trinh vo nghiem");
                }
            }
            else{
                Console.WriteLine($"Phuong trinh co 1 nghiem: {-b / a}");
            }

        }
    }
}