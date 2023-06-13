#include <stdio.h>
#include <string.h>

#include <cctype>
#include <iostream>

struct trangThai {
    int output_be, output_lon, output_bang, output_khac;
};
int ktKytu(char c) {
    if (c == '>') {
        return 1;  // lon la 1
    } else if (c == '=') {
        return 0;  // bang la 0
    } else if (c == '<')
        return -1;  // be la -1
    else
        return -2;  // loi
}
using namespace std;
int main() {
    struct trangThai s[10];
    s[0].output_be = 1;  // -1 la loi
    s[0].output_bang = 5;
    s[0].output_lon = 6;
    s[0].output_khac = 9;
    s[1].output_be = 4;
    s[1].output_bang = 2;
    s[1].output_lon = 3;
    s[1].output_khac = 4;
    s[6].output_be = 8;
    s[6].output_bang = 7;
    s[6].output_lon = 8;
    s[6].output_khac = 8;
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
                state = s[state].output_bang;
                break;
            case 1:
                state = s[state].output_lon;
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
            break;
        }
        if (state == 3) {
            printf("khac\n");
            break;
        }
        if (state == 4) {
            printf("be\n");
            // break;
        }
        if (state == 5) {
            printf("bang\n");
            break;
        }
        if (state == 7) {
            printf("lon hon hoac bang\n");
            break;
        }
        if (state == 8) {
            printf("lon\n");
            break;
        }
        if (state == 9) {
            printf("loi\n");
            break;
        }
    }
}