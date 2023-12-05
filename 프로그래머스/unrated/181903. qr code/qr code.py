def solution(q, r, code):
    answer = []

    for i in range(len(code)) :
        if i%q == r :
            answer.append(code[i])
        else :
            pass
    answer = ''.join(str(s) for s in answer)
    return answer