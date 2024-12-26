def solution(n):
    ans = 0
    i = 1
    while n:
        if i % 3 and '3' not in str(i):
            n -= 1
        i += 1
    ans = i - 1
    return ans