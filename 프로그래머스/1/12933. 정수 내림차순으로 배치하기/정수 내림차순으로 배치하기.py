def solution(n):
    n = list(map(int, str(n)))
    a = sorted(n,reverse=True)
    return int("".join(map(str, a)))