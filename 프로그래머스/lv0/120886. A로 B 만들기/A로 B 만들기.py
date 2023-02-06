def solution(before, after):
    answer = 0
    before = before.replace('"','')
    before = list(before)
    before.sort()
    after = after.replace('"','')
    after = list(after)
    after.sort()
    for i in range(len(before)) :
        if before[i] == after[i] :
            answer = 1
        else : 
            answer = 0
            break
    return answer