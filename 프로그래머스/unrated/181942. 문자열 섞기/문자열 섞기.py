def solution(str1, str2):
    answer = []
    s1 = list(str1)
    s2 = list(str2)
    for i in range(len(str1)):
        answer.insert(i,(s1[i]+s2[i]))
    answer = ''.join(answer)
    return answer