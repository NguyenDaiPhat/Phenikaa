using System;
namespace phatdz
{
    class Program
    {
        static float Generate(float n)
        {
            while (n < 0 || n > 10)
            {
                Console.Write("Nhap lai: ");
                n = float.Parse(Console.ReadLine());
            }
            return n;
        }
        static string chuanHoa(string str)
        {
            str = str.Trim();
            while (str.Contains("  "))
            {
                str = str.Replace("  ", " ");
            }
            string[] tachXau = str.Split(" ");
            string s, outString = "";
            for (int i = 0; i < tachXau.Length; i++)
            {
                s = tachXau[i];
                outString += s.Substring(0, 1).ToUpper() + s.Substring(1).ToLower() + " ";
            }
            outString = outString.Trim();
            return outString;
        }
        struct Student
        {
            public string hoTen;
            public float diemToan;
            public float diemLy;
            public float diemHoa;
            public float diemTrungBinh()
            {
                return (diemHoa + diemLy + diemToan) / 3;
            }
        }
        static void Main(string[] agrs)
        {
            Student student;
            Console.Write("Nhap so luong hoc sinh: ");
            int n = Int32.Parse(Console.ReadLine());
            Student[] A = new Student[n];
            for (int i = 0; i < n; i++)
            {
                Console.Write("Nhap ho va ten hoc sinh thu {0}: ", i + 1);
                A[i].hoTen = chuanHoa(Console.ReadLine());
                Console.Write("Nhap diem toan: ");
                A[i].diemToan = Generate(float.Parse(Console.ReadLine()));
                Console.Write("Nhap diem ly: ");
                A[i].diemLy = Generate(float.Parse(Console.ReadLine()));
                Console.Write("Nhap diem hoa: ");
                A[i].diemHoa = Generate(float.Parse(Console.ReadLine()));
            }
            Console.WriteLine("|-------------------------------------------------------------------|");
            Console.WriteLine("|     Ho Ten     | Diem Toan | Diem Ly | Diem Hoa | Diem Trung Binh |");
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine("|-------------------------------------------------------------------|");
                Console.WriteLine($"| {A[i].hoTen} |   {A[i].diemToan}   |   {A[i].diemLy}   |   {A[i].diemHoa}   |   {A[i].diemTrungBinh()}   |");
            }
            Console.WriteLine("|-------------------------------------------------------------------|");
        }
    }
}