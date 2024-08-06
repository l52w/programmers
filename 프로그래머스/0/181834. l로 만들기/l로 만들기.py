def solution(myString):
    answer = []
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    b = list(myString)
    for i in range(len(b)) : 
        if b[i] in a :
            answer.append('l')
        else :
            answer.append(b[i])
    return ''.join(answer)