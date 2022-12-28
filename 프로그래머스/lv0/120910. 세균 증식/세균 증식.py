def solution(n, t):
    answer = n
    for i in range(t) :
        answer = answer*2
    return answer

# 다른 사람의 풀이
# def solution(n, t):
#     return n*(2**t)
