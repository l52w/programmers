def solution(numbers):
    answer = 0
    n = len(numbers)
    if n < 2:
        return
    numbers.sort()
    if (numbers[0] * numbers[1]) > (numbers[n - 1] * numbers[n - 2]):
        return numbers[0]* numbers[1]
    else:
        return numbers[n - 1]* numbers[n - 2]
    
# 다른 사람의 풀이
# def solution(numbers):
#     numbers.sort()
#     return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
