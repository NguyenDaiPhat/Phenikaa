using System;
namespace Bai2
{
    class Program
    {
        static void Main()
        {
            System.Console.Write("Nhap so luong phan tu mang: ");
            int n = Int32.Parse(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
            {
                System.Console.Write("Phan tu thu {0}: ", i + 1);
                A[i] = Int32.Parse(Console.ReadLine());
            }
            ///
            System.Console.Write("Cac phan tu chan nho hon 20: ");
            int maxIndex = 0;
            for (int i = 0; i < n; i++)
            {
                if (A[i] % 2 == 0 && A[i] != 0 && A[i] < 20)
                    System.Console.Write($"{A[i]} ");
                if (A[i] > A[maxIndex]) maxIndex = i;
            }
            ///
            System.Console.WriteLine();
            System.Console.Write("Nhap x: ");
            int x = int.Parse(Console.ReadLine());
            bool check = false;
            for (int i = n - 1; i >= 0; i--)
            {
                if (A[i] == x)
                {
                    System.Console.WriteLine("Vi tri x xuat hien cuoi cung la: {0}", i + 1);
                    check = true;
                    break;
                }
            }
            if (!check) System.Console.WriteLine("Khong co phan tu x nao trong mang!!!");
            ///
            int[] newArr = new int[A.Length];
            Array.Copy(A, 0, newArr, 0, maxIndex);
            Array.Copy(A, maxIndex + 1, newArr, maxIndex, A.Length - maxIndex - 1);
            A = newArr;
            System.Console.Write("Mang sau khi xoa phan tu lon nhat la: ");
            for (int i = 0; i < n - 1; i++)
                System.Console.Write("{0} ", A[i]);
            ///
            System.Console.WriteLine();
            for (int i = n - 1; i > 0; i--){
                A[i] = A[i-1];
            }
            A[0] = x;
            System.Console.Write("Mang sau khi chen x vao vi tri dau la: ");
            for (int i = 0; i < n;i++)System.Console.Write($"{A[i]} ");
        }
    }
}