def solution(numer1, denom1, numer2, denom2):
    answer = []
    import math
    a = (numer1*denom2) + (numer2*denom1)
    b = denom1 * denom2
    c = math.gcd(a,b)
    return [a//c,b//c]