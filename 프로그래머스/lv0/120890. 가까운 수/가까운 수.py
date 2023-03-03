def solution(array, n):
    box = []
    array.sort()
    for i in array:
        box.append(abs(n-i))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
    return answer

# 풀이 실패
# def solution(array, n):
#     answer = 0
#     a = abs(array[-1])
#     for i in range(len(array)) :
#         if abs(n - array[i]) < a :
#             a = abs(n-array[i])
#             answer = array[i]
#         elif abs(n-array[i]) == a :
#             a = abs(n-array[i])
#             answer = array[i-1]
#     return answer
