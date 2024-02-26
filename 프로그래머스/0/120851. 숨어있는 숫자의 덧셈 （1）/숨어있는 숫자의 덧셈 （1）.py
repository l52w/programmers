def solution(my_string):
    answer = 0
    a = list(my_string)
    for i in range(len(a)) :
        if a[i] in '1234567890' :
            answer += int(a[i])
        else :
            pass
    return answer