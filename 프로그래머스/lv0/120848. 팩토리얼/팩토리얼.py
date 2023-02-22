def solution(n):
    answer = 0
    isum = 1
    for i in range(1,11) :
        isum *= i
        if isum == n :
            return i
        elif isum > n :
            return i-1
            break