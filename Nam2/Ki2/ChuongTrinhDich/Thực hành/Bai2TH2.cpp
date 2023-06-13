#include <stdio.h>
#include <string.h>

#include <cctype>
#include <iostream>

struct trangThai {
    int output_chuso, output_khac, output_congtru, output_cham, output_e;
};
int ktKytu(char c) {
    if (c >= '0' && c <= '9') {
        return 0;  // So la 0
    } else if (c == 'E')
        return 1;  // E la 1
    else if (c == '.')
        return 2;
    else if (c == '+' || c == '-')
        return 3;
    else
        return 4;
}
using namespace std;
int main() {
    struct trangThai s[12];
    s[0].output_chuso = 2;
    s[0].output_e = 11;
    s[0].output_cham = 11;
    s[0].output_congtru = 1;
    s[0].output_khac = 11;

    s[1].output_chuso = 2;
    s[1].output_e = 11;
    s[1].output_cham = 11;
    s[1].output_congtru = 1;
    s[1].output_khac = 11;

    s[2].output_chuso = 2;
    s[2].output_e = 5;
    s[2].output_cham = 3;
    s[2].output_congtru = 10;
    s[2].output_khac = 10;

    s[3].output_chuso = 4;
    s[3].output_e = 10;
    s[3].output_cham = 10;
    s[3].output_congtru = 10;
    s[3].output_khac = 10;

    s[4].output_chuso = 4;
    s[4].output_e = 5;
    s[4].output_cham = 9;
    s[4].output_congtru = 9;
    s[4].output_khac = 9;

    s[5].output_chuso = 7;
    s[5].output_e = 9;
    s[5].output_cham = 9;
    s[5].output_congtru = 6;
    s[5].output_khac = 9;

    s[6].output_chuso = 7;
    s[6].output_e = 9;
    s[6].output_cham = 9;
    s[6].output_congtru = 9;
    s[6].output_khac = 9;

    s[7].output_chuso = 7;
    s[7].output_e = 8;
    s[7].output_cham = 8;
    s[7].output_congtru = 8;
    s[7].output_khac = 8;
    char token[100];
    printf("Nhap vao 1 day\n");
    scanf("%s", &token);
    char t[10] = "+";
    strcat(token, t);
    int state = 0;
    for (int i = 0; i < strlen(token); i++) {
        int kt = ktKytu(token[i]);
        switch (kt) {
            case 0:
                state = s[state].output_chuso;
                break;
            case 1:
                state = s[state].output_e;
                break;
            case 2:
                state = s[state].output_cham;
                break;
            case 3:
                state = s[state].output_congtru;
                break;
            case 4:
                state = s[state].output_khac;
                break;
        }
        if (state == 8) {
            printf("so thuc mu\n");
            // return 0;
        }
        if (state == 9) {
            printf("so thuc \n");
            // return 0;
        }
        if (state == 10) {
            printf("so nguyen\n");
            // return 0;
        }
        if (state == 11) {
            printf("Loi cu phap\n");
            return 0;
        }
    }
}