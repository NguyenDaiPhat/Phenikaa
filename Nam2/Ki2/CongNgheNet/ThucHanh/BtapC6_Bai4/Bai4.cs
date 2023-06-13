using System;
namespace Bai4
{
    class Program
    {
        static void Main(string[] args)
        {
            // 
            VanDongVien p = new VanDongVien("Nguyen Van A", 25, "Thang 1", 70.5, 1.8);

            // 
            Console.WriteLine("Thong tin cua van dong vien:");
            Console.WriteLine(p);

            // 
            Console.Write("Nhap so luong van dong vien: ");
            int n = int.Parse(Console.ReadLine());

            // 
            VanDongVien[] arr = new VanDongVien[n];
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine("Nhap thong tin van dong vien thu {0}:", i + 1);
                arr[i] = VanDongVien.Nhap();
            }

            // 
            Console.WriteLine("Danh sach van dong vien:");
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(arr[i]);
            }

            // Sắp xếp mảng vận động viên theo thứ tự tăng dần và hiển thị danh sách đã sắp xếp
            Array.Sort(arr);
            Console.WriteLine("Danh sach van dong vien sau khi sap xep:");
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(arr[i]);
            }

            Console.ReadKey();
        }
    }
}