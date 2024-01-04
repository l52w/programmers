def solution(myString):
    answer = []
    a = myString.split('x')
    for i in range(len(a)) :
        answer.append(len(a[i]))
    return answer