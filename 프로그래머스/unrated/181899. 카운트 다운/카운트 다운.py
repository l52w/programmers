def solution(start_num, end_num):
    answer = []
    for i in range(start_num+1) :
        if i>=end_num and i<=start_num :
            answer.append(i)
    return answer[::-1]