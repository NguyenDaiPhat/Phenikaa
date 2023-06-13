using System;
namespace HelloWorld
{
    class Bai5
    {
        public void SapXep()
        {
            Console.Write("Nhap n so phan tu mang: ");
            int n, min = int.MaxValue, max = int.MinValue;
            n = Int32.Parse(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
            {
                A[i] = Int32.Parse(Console.ReadLine());
                min = Math.Min(min, A[i]);
                max = Math.Max(max, A[i]);
            }
            Console.WriteLine("min: " + min);
            Console.WriteLine("max: " + max);
            for (int i = 0; i < n - 1; i++)
                for (int j = i + 1; j < n; j++)
                {
                    if (A[i] > A[j])
                    {
                        int tg = A[i];
                        A[i] = A[j];
                        A[j] = tg;
                    }
                }
            Console.WriteLine("Day tang dan:");
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(A[i]);
            }
            Console.WriteLine("Day giam dan:");
            for (int i = 0; i < n - 1; i++)
                for (int j = i + 1; j < n; j++)
                {
                    if (A[i] < A[j])
                    {
                        int tg = A[i];
                        A[i] = A[j];
                        A[j] = tg;
                    }
                }
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(A[i]);
            }

        }
    }
}