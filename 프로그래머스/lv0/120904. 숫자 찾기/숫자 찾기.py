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