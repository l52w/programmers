def solution(array):
    answer = 0
    array.sort()
    n = (len(array)//2)
    answer = array[n]
    return answer

# 다른 사람의 풀이
# def solution(array):
#     return sorted(array)[len(array) // 2]
