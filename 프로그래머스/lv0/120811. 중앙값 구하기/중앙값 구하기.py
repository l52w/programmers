def solution(array):
    answer = 0
    array.sort()
    n = (len(array)//2)
    answer = array[n]
    return answer