def solution(array):
    answer = 0
    array = list(map(str,array))
    for i in range(len(array)) :
        if '7' in array[i] :
            a = array[i].count('7')
            answer += a
        else :
            pass
    return answer