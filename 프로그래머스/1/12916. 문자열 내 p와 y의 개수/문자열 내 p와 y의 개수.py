def solution(s):
    a,b = 0,0
    for i in range(len(s)) :
        if s[i] == 'p' or s[i] == 'P' :
            a += 1
        elif s[i] == 'y' or s[i] == 'Y' :
            b += 1
    if a == b :
        return True
    else :
        return False