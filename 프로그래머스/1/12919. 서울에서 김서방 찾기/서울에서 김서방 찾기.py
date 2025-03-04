def solution(seoul):
    answer = ['김서방은 ']
    for i in range(len(seoul)) :
        if seoul[i] == "Kim" :
            answer.append(str(i))
    answer.append('에 있다')
    return ''.join(answer)