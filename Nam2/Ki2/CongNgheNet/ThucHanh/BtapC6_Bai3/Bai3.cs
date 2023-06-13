using System;
namespace Bai3
{
    class Program
    {
        static void Main()
        {
            System.Console.Write("Nhap mot chuoi: ");
            string str = Console.ReadLine();
            string[] words = str.Split(' ');
            Console.WriteLine("So tu trong chuoi la: " + words.Length);
            ///
            str = str.Replace(" ", "");
            System.Console.WriteLine("Chuoi sau khi xoa khoang cach la: " + str);
            ///
            System.Console.Write("Nhap ki tu c: ");
            char c = char.Parse(Console.ReadLine());
            int index = str.IndexOf(c); // Tìm vị trí xuất hiện đầu tiên của kí tự 's' trong chuỗi
            if (index != -1)
            {
                Console.WriteLine($"Vi tri xuat hien dau tien cua {c} la: " + index);
                index = str.IndexOf(c, index + 1);
                if (index != -1)
                {
                    System.Console.Write($"Cac vi tri tiep theo ma {c} xua hien la: ");
                    while (index != -1)
                    {
                        System.Console.Write(index + " ");
                        index = str.IndexOf(c, index + 1);
                    }
                }
            }
            else System.Console.WriteLine($"Khong co ki tu {c} nao xuat hien");

        }
    }
}