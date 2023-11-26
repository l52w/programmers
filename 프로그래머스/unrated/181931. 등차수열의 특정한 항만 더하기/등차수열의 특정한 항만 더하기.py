def solution(a, d, included):
    answer = 0
    true = True
    false = False
    b=[]
    for i in range(len(included)) :
        c = a + i*d
        b.insert(i,c)
    for i in range(len(included)) :
        if included[i] == true :
            answer += b[i]
        else :
            pass
    return answer