#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int slice, int n) {
    int answer = 1;
    int temp = slice;
    while ( n > slice) {
        slice += temp;
        answer ++;
    }
    return answer;
}