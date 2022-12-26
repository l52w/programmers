def solution(money):
    answer = []
    n = int(money/5500)
    answer.insert(0,n)
    answer.insert(1,money-5500*n)
    return answer