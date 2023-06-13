#include <stdio.h>
#include <string.h>

#include <cctype>
#include <iostream>

struct trangThai {
    int output_be, output_lon, output_bang, output_chucai, output_chuso, output_khac;
};
int ktKytu(char c) {
    if (c == '>') {
        return 1;  // lon la 1
    } else if (c == '=') {
        return 0;  // bang la 0
    } else if (c == '<')
        return -1;  // be la -1
    else if (isalpha(c))
        return 2;  // chu cai la 2
    else if (isdigit(c))
        return 3;  // chuso la 3
    else
        return -2;  // loi
}
using namespace std;
int main() {
    struct trangThai s[12];
    s[0].output_be = 1;  // -1 la loi
    s[0].output_bang = 5;
    s[0].output_lon = 6;
    s[0].output_chucai = 10;
    s[0].output_chuso = 9;
    s[0].output_khac = 9;
    s[1].output_be = 4;
    s[1].output_bang = 2;
    s[1].output_lon = 3;
    s[1].output_chucai = 4;
    s[1].output_chuso = 4;
    s[1].output_khac = 4;
    s[6].output_be = 8;
    s[6].output_bang = 7;
    s[6].output_lon = 8;
    s[6].output_chucai = 8;
    s[6].output_chuso = 8;
    s[6].output_khac = 8;
    s[10].output_be = 11;
    s[10].output_bang = 11;
    s[10].output_lon = 11;
    s[10].output_chucai = 10;
    s[10].output_chuso = 10;
    s[10].output_khac = 11;
    char token[100];
    printf("Nhap vao 1 day\n");
    scanf("%s", &token);
    char t[10] = "+";
    strcat(token, t);
    int state = 0;
    for (int i = 0; i < strlen(token); i++) {
        int kt = ktKytu(token[i]);
        // cout << kt;
        switch (kt) {
            case 0:
                state = s[state].output_bang;
                break;
            case 1:
                state = s[state].output_lon;
                break;
            case 2:
                state = s[state].output_chucai;
                break;
            case 3:
                state = s[state].output_chuso;
                break;
            case -1:
                state = s[state].output_be;
                break;
            case -2:
                state = s[state].output_khac;
                break;
        }
        if (state == 2) {
            printf("be hon hoac bang\n");
            // break;
        }
        if (state == 3) {
            printf("khac\n");
            // break;
        }
        if (state == 4) {
            printf("be\n");
            // break;
        }
        if (state == 5) {
            printf("bang\n");
            // break;
        }
        if (state == 7) {
            printf("lon hon hoac bang\n");
            // break;
        }
        if (state == 8) {
            printf("lon\n");
            // break;
        }
        if (state == 11) {
            printf("ten\n");
            // break;
        }
        if (state == 9) {
            printf("loi\n");
            break;
        }
    }
}