#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len, int n){
    int a = 0;
    int b = 101;
    int answer = 0;
    for (int i = 0; i < array_len ; i ++){
        int k = abs(array[i] - n);
        if (k <= b){   
            if (k < b){
                a = array[i]; 
                b = k;
            }
            else{
                if(a > array[i]) a = array[i];
            }
        }
    }
    answer = a;
    return answer;
}
