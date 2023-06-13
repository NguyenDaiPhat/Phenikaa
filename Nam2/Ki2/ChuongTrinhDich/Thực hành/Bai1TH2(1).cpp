#include <stdio.h>
#include <string.h>

#include <cctype>
#include <iostream>

struct trangThai {
    int output_chucai, output_so, output_khac;
};
int ktKytu(char c) {
    if (((c >= 'a') && (c <= 'z')) || ((c >= 'A') && (c <= 'Z'))) {
        return 1;  // Chu cai la 1
    } else if (c >= '0' && c <= '9') {
        return 0;  // So la 0
    } else
        return -1;  // Khac la -1
}
using namespace std;
int main() {
    struct trangThai s[2];
    s[0].output_so = -1;  // -1 la loi
    s[0].output_chucai = 1;
    s[0].output_khac = -1;
    s[1].output_so = 1;
    s[1].output_chucai = 1;
    s[1].output_khac = 2;
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
                state = s[state].output_so;
                break;
            case 1:
                state = s[state].output_chucai;
                break;
            case -1:
                state = s[state].output_khac;
                break;
        }
        if (state == 2){
            printf("Day da nhap la 1 ten\n");
        }
        if (state == -1) {
            printf("Loi cu phap\n");
        }
    }
}