def solution(sides):
    answer = 0
    sides = sorted(sides)
    i = sides[1]+1
    while i < sides[0]+sides[1] :
        i += 1
        answer += 1
    answer += sides[0]
    return answer