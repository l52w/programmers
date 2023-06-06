def solution(numbers):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, num in enumerate(num) :
        numbers = numbers.replace(num, str(index))
    return int(numbers)