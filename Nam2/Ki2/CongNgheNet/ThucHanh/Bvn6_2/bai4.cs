using System;
namespace HelloWorld
{
    class Bai4
    {
        public void Mang()
        {
            Console.Write("Nhap n so phan tu mang: ");
            int n;
            n = Int32.Parse(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
            {
                A[i] = Int32.Parse(Console.ReadLine());
            }
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(A[i]);
            }
            int k;
            bool kt = false;
            Console.Write("Nhap so k: ");
            k = Int32.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                if (A[i] == k)
                {
                    Console.WriteLine("Phan tu k co trong mang");
                    kt = true;
                }
            }
            if (!kt) Console.WriteLine("Phan tu k khong co trong mang");
        }
    }
}