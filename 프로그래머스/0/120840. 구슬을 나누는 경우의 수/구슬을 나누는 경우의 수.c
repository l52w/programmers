#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int balls, int share){
    long long a=1,i,b=1;
    for(i=balls; i>balls-share; i--) a=a*i/b++;
    return a;
}