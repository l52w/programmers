def solution(myString, pat):
    answer = 0
    a = list(myString)
    b = []
    for i in range(len(a)) :
        if a[i] == "A" :
            b.insert(i,"B")
        else :
            b.insert(i,"A")
    c = ''.join(s for s in b)
    if pat in c :
        answer = 1
    else :
        answer = 0
    return answer