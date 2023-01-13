def solution(num, k):
    answer = 0
    num = list(map(int, str(num)))
    for i in range(len(num)) :
        if (k in num) :
            if num[i] == k:
                answer = i+1
                break
        else :
            answer = -1
    return answer

# 다른 사람의 풀이
# def solution(num, k):
#     answer = (str(num).find(str(k))+1)
#     if answer == 0:
#         answer = -1
#     return answer
