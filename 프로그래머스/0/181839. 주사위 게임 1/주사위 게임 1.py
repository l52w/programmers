def solution(a, b):
    answer = 0
    if a % 2 != 0 and b%2!=0 :
        return a**2 + b**2
    elif (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0) :
        return 2 * (a+b)
    else :
        if a > b :
            return a-b
        else :
            return b-a