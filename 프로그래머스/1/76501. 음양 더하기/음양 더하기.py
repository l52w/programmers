def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)) :
        if signs[i] == False :
            answer.append(-absolutes[i])
        else :
            answer.append(absolutes[i])
    return sum(answer)