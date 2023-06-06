def solution(numbers):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, num in enumerate(num) :
        numbers = numbers.replace(num, str(index))
    return int(numbers)

# for index, num in enumerate(num) ==> 0 'zero', 1 'one', ...
# numbers = numbers.replace(num, str(index)) ==> 'zero'->'0' , 'one'->'1', ...
# return int(numbers) ==> 0,1, ...

# enumerate내장함수
# for i, letter in enumberate(['A','B','C'], start=1) :
#     print(i, letter)
#
# 1 A
# 2 B
# 3 C
