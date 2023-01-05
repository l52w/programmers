def solution(hp):
    a = hp // 5
    b = (hp - (a*5)) // 3
    c = (hp - (a*5) - (b*3)) // 1
    return a+b+c

# 다른 사람의 풀이
# def solution(hp):    
#     return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
