#include <stdio.h>

int main() {
    int Q, D, N, P;
    int t, a;
    scanf("%d", &t);

    for(int i=0; i<t; i++){
        scanf("%d", &a);
        Q = a / 25;
        D = a%25 / 10;
        N = a%25%10 / 5;
        P = a%25%10%5 / 1;
        printf("%d %d %d %d \n", Q, D, N, P);
    }
}