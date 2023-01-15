def solution(numbers, direction):
    a,b = [],[]
    if direction == "right" :
        a.append(numbers[-1])
        b = numbers[:-1]
        return a+b
    if direction == "left" :
        a.append(numbers[0])
        b = numbers[1:]
        return b+a
    
    
# 다른 사람의 풀이
# from collections import deque
# def solution(numbers, direction):
#     numbers = deque(numbers)
#     if direction == 'right':
#         numbers.rotate(1)
#     else:
#         numbers.rotate(-1)
#     return list(numbers)
