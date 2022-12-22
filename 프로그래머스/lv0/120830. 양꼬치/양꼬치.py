def solution(n, k):
    answer = 0
    m = int(n/10)
    return n*12000 + k*2000 - m*2000

# 다른 사람의 풀이
# def solution(n, k):
#     return n * 12000 + (k - n // 10) * 2000
