def solution(n):
    answer = []
    answer.append(n)
    for i in range(n) :
        if answer[i] == 1 :
            break
        else :
            if answer[i]%2 == 0:
                answer.append(answer[i]//2)
            elif answer[i]%2 != 0 :
                answer.append(3*answer[i]+1)
    return answer