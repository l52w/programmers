def solution(spell, dic):
    answer = []
    num = 0
    for i in range(len(dic)) :
        for j in range(len(spell)) :
            if spell[j] in dic[i] :
                num += 1
            else :
                pass
        if num >= len(spell) :
            answer.append('a')
        else :
            answer.append('b')
        num = 0
    if 'a' in answer :
        return 1
    else :
        return 2
