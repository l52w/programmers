#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* rsp) {
    char a[1000] = {0,};
    for(int i=0; i<strlen(rsp); i++){
        if(rsp[i] == '2') a[i] = '0';
        else if(rsp[i] == '0') a[i] = '5';
        else if(rsp[i] == '5') a[i] = '2';
        printf("%c-%c\n",rsp[i],a[i]);
    }
    return a;
}