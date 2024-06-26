#include <stdio.h>
#include <string.h>

int main() {
    char a[101];
    scanf("%s", a);
    int b = strlen(a)/2;
    int c = 0;

    for(int i=0; i<=b; i++){
        if(a[i] !=a[strlen(a)-i-1]){
            printf("0");
            return 0;
        }
    }
    printf("1");
    return 0;
}