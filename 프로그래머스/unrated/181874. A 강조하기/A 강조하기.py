def solution(myString):
    answer = []
    a = myString.lower()
    b = list(a)
    for i in range(len(b)) :
        if b[i] == 'a' :
            answer.insert(i,'A')
        else :
            answer.insert(i,b[i])
    return ''.join(answer)