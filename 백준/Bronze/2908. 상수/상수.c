#include <stdio.h>

int main() {
    int A, B;
    scanf("%d %d", &A, &B);

    int newA = 0;
    while(A > 0) {
        newA = newA * 10 + (A % 10);
        A /= 10;
    }

    int newB = 0;
    while(B > 0) {
        newB = newB * 10 + (B % 10);
        B /= 10;
    }

    if(newA > newB) printf("%d", newA);
    else printf("%d", newB);
}