def solution(arr, flag):
    answer = []
    for i in range(len(arr)) :
        if flag[i] == True :
            for j in range(arr[i]*2) :
                answer.append(arr[i])
        elif flag[i] == False :
            a = arr[i]
            del answer[-a:]
    return answer