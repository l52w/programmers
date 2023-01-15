def solution(rsp):
    answer = ''
    rsp = list(rsp)
    a=[]
    for i in range(len(rsp)):
        if rsp[i] == "2" :
            a.append("0")
        elif rsp[i] == "0" :
            a.append("5")
        else :
            a.append("2")
    answer = ''.join(map(str, a))
    return answer