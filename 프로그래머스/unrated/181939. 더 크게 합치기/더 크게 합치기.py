def solution(a, b):
    c = str(a)+str(b)
    d = str(b)+str(a)
    if c < d :
        return int(d)
    else :
        return int(c)