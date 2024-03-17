#include <stdio.h>

int main() {
    int x,n;
    scanf("%d", &x);
    scanf("%d", &n);
    int sum = 0;
    for(int i=0; i<n; i++){
        int a,b;
        scanf("%d %d", &a,&b);
        sum += a*b;
    }
    if(sum==x) printf("Yes");
    else printf("No");
}