#include <iostream>
#include <string>

int main()
{
    std::string str;
    std::cout << "Nhap xau: ";
    std::getline(std::cin, str);
    std::cout << "Xau vua nhap la: " << str << std::endl;
    return 0;
}
