def solution(s):
    answer = ''
    a,b = [],[]
    s = list(s)
    for i in range(len(s)) :
        if s[i] in a :
            b.append(s[i])
        else :
            a.append(s[i])
    answer = [i for i in s if i not in b]
    answer.sort()
    answer = ''.join(map(str,answer))
    return answer