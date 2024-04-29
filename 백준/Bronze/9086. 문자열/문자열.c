#include <stdio.h>
#include <string.h>

int main() {
    int a; 
    scanf("%d", &a);
    
    char b[101];
    while(a--){
        scanf("%s", b);
        printf("%c%c \n", b[0],b[strlen(b)-1]);
    }
}