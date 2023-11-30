def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        i = str(i)
        if '1' in i or '2' in i or '3' in i or '4' in i or '6' in i or '7' in i or '8'in i or '9' in i :
            pass
        else :
            if ('5' in i) or ('0' in i) :
                answer.append(int(i))
            else :
                pass
    if len(answer) == 0 :
        answer.append(-1)
    return answer