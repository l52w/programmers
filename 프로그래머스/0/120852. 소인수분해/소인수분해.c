#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(10000);
    int a,b;
    for(b=0,a=2;n>1;a++) {
        if(!(n%a)) {
            answer[b++] = a;
            for(;!(n%a);n/=a);
        }
    }
    return answer;
}