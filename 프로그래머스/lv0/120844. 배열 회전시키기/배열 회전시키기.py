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