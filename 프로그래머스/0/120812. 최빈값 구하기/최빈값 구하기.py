def solution(array):
    from collections import Counter
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    elif a[0][1] == a[1][1]:
        return -1
    else :
        return a[0][0]