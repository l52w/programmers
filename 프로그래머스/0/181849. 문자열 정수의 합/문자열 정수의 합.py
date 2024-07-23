def solution(num_str):
    answer = 0
    for i in range(len(list(num_str))) :
        answer += int(list(num_str)[i])
    return answer