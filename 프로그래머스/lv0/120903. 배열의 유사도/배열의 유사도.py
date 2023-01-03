def solution(s1, s2):
    answer = 0
    for i in range(len(s1)):
        for j in range(len(s2)) :
            x,y = s1[i],s2[j]
            if x == y :    
                answer += 1
    return answer

# 다른 사람의 풀이
# def solution(s1, s2):
#     return len(set(s1)&set(s2));
