def solution(rank, attendance):
    answer =0
    a = []
    for i in range(len(rank)):
        if attendance[i]:
            a.append([rank[i], i])
    a.sort(key = lambda v : v[0])
    return 10000 * a[0][1] + 100 * a[1][1] + a[2][1]