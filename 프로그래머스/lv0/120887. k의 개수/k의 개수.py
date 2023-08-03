def solution(i, j, k):
    answer = 0
    array = []

    for n in range(i,j+1) :
        array.append(n)
    array = list(map(str,array))
    for m in array :
        if str(k) in m :
            a = m.count(str(k))
            answer += a

    return answer