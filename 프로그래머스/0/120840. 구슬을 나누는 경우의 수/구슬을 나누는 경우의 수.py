def solution(balls, share):
    from math import factorial as f
    return f(balls) / (f(balls-share)*f(share))