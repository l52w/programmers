def solution(rsp):
    answer = []
    rsp = list(rsp)
    for i in range(len(rsp)):
        if rsp[i] == "2" :
            answer.insert(i, '0')
        elif rsp[i] == "0" :
            answer.insert(i, '5')
        else :
            answer.insert(i, '2')
    return ''.join(answer)