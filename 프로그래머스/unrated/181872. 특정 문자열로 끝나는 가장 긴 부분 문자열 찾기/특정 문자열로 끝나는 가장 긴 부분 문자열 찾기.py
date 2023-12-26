def solution(myString, pat):
    answer = 0
    for i in range(len(myString)) :
        if myString[i] in pat :
            answer = i
    return myString[:answer+1]