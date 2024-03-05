def solution(array, n):
    array = sorted(array)
    answer = []
    for i in array :
        answer.append(abs(n-i))
    return array[answer.index(min(answer))]