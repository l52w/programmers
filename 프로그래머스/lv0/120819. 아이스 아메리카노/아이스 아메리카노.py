def solution(money):
    answer = []
    n = int(money/5500)
    answer.insert(0,n)
    answer.insert(1,money-5500*n)
    return answer

# 다른 사람의 풀이
# def solution(money):
#     answer = [money // 5500, money % 5500]
#     return answer
