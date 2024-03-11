#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    int b[a];
    for(int i=0; i<a; i++) scanf("%d", &b[i]);
    int min = b[0], max = b[0];
    for(int j=0; j<a; j++){
        if(b[j] < min) min = b[j];
        if(b[j] > max) max = b[j];
    }
    printf("%d %d", min, max);
}