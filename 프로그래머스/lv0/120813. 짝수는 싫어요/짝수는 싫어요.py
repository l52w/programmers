def solution(n):
    answer = []
    for i in range(n+1) :
        if i%2 != 0 :
            answer.append(i)
    return answer

# 다른 사람의 풀이
# def solution(n):
#     return [i for i in range(1, n+1, 2)]
