from math import gcd 
def solution(dots):
    (x1, y1) = dots[0]
    for j in range(1, 4):
        (x2, y2) = dots[j]
        g1 = gcd(x2-x1, y2-y1)
        slope1 = ((x2-x1)/g1, (y2-y1)/g1) if (x2-x1)/g1 >=0 else ((x1-x2)/g1, (y1-y2)/g1)
        rest = [dots[k] for k in (1, 2, 3) if k != j]
        (x3, y3) = (rest[0][0], rest[0][1])
        (x4, y4) = (rest[1][0], rest[1][1])
        g2 = gcd(x4-x3, y4-y3)
        slope2 = ((x4-x3)/g2, (y4-y3)/g2) if (x4-x3)/g2 >=0 else ((x4-x3)/g2, (y4-y3)/g2)
        if slope1 == slope2: return 1
    return 0