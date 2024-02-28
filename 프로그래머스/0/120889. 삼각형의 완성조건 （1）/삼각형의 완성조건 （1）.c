#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sides_len은 배열 sides의 길이입니다.
int compare(const void* a, const void* b){
    int num1 = *(int*) a;
    int num2 = *(int*) b;
    if (num1>num2) return 1;
    if (num1<num2) return -1;
    return 0;
}
int solution(int sides[], size_t sides_len){
    qsort(sides,sides_len,sizeof(int), compare);
    if (sides[0]+sides[1] >sides[2]) return 1;
    else return 2;

}
