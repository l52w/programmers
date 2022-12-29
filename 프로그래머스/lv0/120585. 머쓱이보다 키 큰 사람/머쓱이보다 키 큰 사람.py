def solution(array, height):
    answer = 0
    for i in range(len(array)) :
        if array[i] > height :
            answer += 1
    return answer

# 다른 사람의 풀이
# def solution(array, height):
#     array.append(height)
#     array.sort(reverse=True)
#     return array.index(height)
