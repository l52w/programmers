def solution(my_string, alp):
    answer = []
    a = list(my_string)
    for i in range(len(a)) :
        if a[i] == alp :
            answer.insert(i,alp.upper())
        else :
            answer.insert(i,a[i])
    return ''.join(answer)