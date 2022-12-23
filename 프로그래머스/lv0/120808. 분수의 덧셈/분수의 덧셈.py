def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    m = num1 * num2
    j = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    start = max(m, j)
    x = 1
    
    for num in range(start, 0, -1):
        if m % num == 0 and j % num == 0:
            x = num
            break
    

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [j / x, m / x]
    return answer

# 다른 사람의 풀이
# import math
# def solution(denum1, num1, denum2, num2):
#     denum = denum1 * num2 + denum2 * num1
#     num = num1 * num2
#     gcd = math.gcd(denum, num)
#     return [denum//gcd, num//gcd]
