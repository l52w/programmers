def solution(numLog):
    answer = []
    for i in range(1,len(numLog)):
        if numLog[i] - numLog[i-1] == 1 :
            answer.append('w')
        elif numLog[i] - numLog[i-1] == -1 :
            answer.append('s')
        elif numLog[i] - numLog[i-1] == 10 :
            answer.append('d')
        elif numLog[i] - numLog[i-1] == -10 :
            answer.append('a')
        elif numLog[i] - numLog[i-1] == 2 :
            answer.append('w')
        elif numLog[i] - numLog[i-1] == -2 :
            answer.append('s')
    answer = ''.join(s for s in answer)
    return answer