def solution(strArr):
    answer = [len(i) for i in strArr]
    a = []
    for i in set(answer):
        a.append(answer.count(i))
    
    return max(a)