def solution(numbers, direction):
    answer = []
    if direction=='right':
        answer.insert(0, numbers[-1])
        for i in range(len(numbers)-1) :
            answer.insert(i+1, numbers[i])
    else :
        answer.insert(len(numbers), numbers[0])
        for i in range(len(numbers)):
            answer.insert(i, numbers[i])
        answer.remove(answer[0])
    return answer