def solution(n, k):
    answer = []
    a,b = 1,1
    while a <= n :
        a = k*b
        b += 1
        answer.append(a)
    return answer[:-1]