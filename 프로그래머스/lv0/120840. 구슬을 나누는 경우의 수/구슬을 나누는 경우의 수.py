def solution(balls, share):
    a,b = 1,1
    for i in range(share) :
        a *= balls-i
    for i in range(share) :
        b *= (i+1)
    return a/b