def solution(strArr):
    answer = []
    for i in range(len(strArr)) :
        if i%2 == 0 :
            answer.insert(i,strArr[i].lower())
        else :
            answer.insert(i,strArr[i].upper())
    return answer