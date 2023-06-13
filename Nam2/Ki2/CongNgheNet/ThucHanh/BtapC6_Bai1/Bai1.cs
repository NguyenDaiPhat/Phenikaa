using System;
namespace Bai1
{
    class Program
    {
        static int GCD(int a, int b)
        {
            while (b != 0)
            {
                int r = a % b;
                a = b;
                b = r;
            }
            return a;
        }
        public static int Factorial(int n)
        {
            int result = 1;
            for (int i = 1; i <= n; i++)
            {
                result *= i;
            }
            return result;
        }
        public static bool IsPrime(int n)
        {
            if (n <= 1)
            {
                return false;
            }
            for (int i = 2; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        static void Main()
        {
            System.Console.Write("Nhap n: ");
            int n = Int32.Parse(Console.ReadLine());
            System.Console.WriteLine($"Tong 1 den n la: {(n * (n + 1)) / 2}");
            double tongBinhPhuong = 0;
            double tongThuong = 0;
            for (int i = 1; i <= n; i++)
            {
                tongBinhPhuong += Math.Pow(i, 2);
                tongThuong += 1 / (2.0 * i);
            }
            System.Console.WriteLine($"Tong binh phuong 1 den n la: {tongBinhPhuong}");
            System.Console.WriteLine($"Tong cac thuong 1/2 den 1/2n la: {tongThuong}");
            System.Console.WriteLine("Nhap 2 so a va b: ");
            int a = Int32.Parse(Console.ReadLine());
            int b = Int32.Parse(Console.ReadLine());
            int gcd = GCD(a, b);
            System.Console.WriteLine($"Uoc chung lon nhat a b la: {gcd}");
            System.Console.WriteLine($"Boi chung nho nhat a b la: {a * b / gcd}");
            System.Console.WriteLine($"n! la: {Factorial(n)}");
            if (IsPrime(n))
            {
                Console.WriteLine($"{n} la so nguyen to.");
            }
            if (n <= 2) System.Console.WriteLine("Khong co so nguyen to nao be hon n");
            else
            {
                System.Console.Write("Cac so nguyen to be hon n la: ");
                for (int i = 2; i < n; i++)
                    if (IsPrime(i)) System.Console.Write($"{i} ");
            }
        }
    }
}