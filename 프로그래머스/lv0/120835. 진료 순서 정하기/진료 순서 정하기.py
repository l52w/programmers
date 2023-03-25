def solution(emergency):
    answer = []
    a = sorted(emergency)
    a.sort(reverse=True)
    for i in emergency :
        answer.append(a.index(i)+1)
    return answer