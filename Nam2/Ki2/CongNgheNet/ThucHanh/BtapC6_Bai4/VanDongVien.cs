using System;
namespace Bai4
{
    class VanDongVien : IComparable<VanDongVien>
    {
        public string hoten;
        public int tuoi;
        public string monthidau;
        public double cannang;
        public double chieucao;

        public VanDongVien()
        {
        }

        public VanDongVien(string hoten, int tuoi, string monthidau, double cannang, double chieucao)
        {
            this.hoten = hoten;
            this.tuoi = tuoi;
            this.monthidau = monthidau;
            this.cannang = cannang;
            this.chieucao = chieucao;
        }

        public static VanDongVien Nhap()
        {
            Console.Write("Nhap ho ten: ");
            string hoten = Console.ReadLine();
            Console.Write("Nhap tuoi: ");
            int tuoi = int.Parse(Console.ReadLine());
            Console.Write("Nhap mon thi dau: ");
            string monthidau = Console.ReadLine();
            Console.Write("Nhap can nang: ");
            double cannang = double.Parse(Console.ReadLine());
            Console.Write("Nhap chieu cao: ");
            double chieucao = double.Parse(Console.ReadLine());
            return new VanDongVien(hoten, tuoi, monthidau, cannang, chieucao);
        }

        public override string ToString()
        {
            return string.Format("Ho ten: {0}, Tuoi: {1}, Mon thi dau: {2}, Can nang: {3}, Chieu cao: {4}", hoten, tuoi, monthidau, cannang, chieucao);
        }

        public int CompareTo(VanDongVien other)
        {
            if (this.chieucao > other.chieucao)
                return 1;
            else if (this.chieucao < other.chieucao)
                return -1;
            else
            {
                if (this.cannang > other.cannang)
                    return 1;
                else if (this.cannang < other.cannang)
                    return -1;
                else
                    return 0;
            }
        }

        public static bool operator >(VanDongVien a, VanDongVien b)
        {
            return a.CompareTo(b) > 0;
        }

        public static bool operator <(VanDongVien a, VanDongVien b)
        {
            return a.CompareTo(b) < 0;
        }
    }
}