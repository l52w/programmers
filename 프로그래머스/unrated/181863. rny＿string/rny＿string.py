def solution(rny_string):
    answer = []
    a = list(rny_string)
    for i in range(len(a)) :
        if a[i] == 'm' :
            answer.insert(i,'rn')
        else :
            answer.insert(i,a[i])
    answer = ''.join(s for s in answer)
    return answer