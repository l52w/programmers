def solution(num_list):
    answer = []
    j = 0
    h = 0
    for i in num_list :
        if i%2==0 :
            j += 1
        else :
            h += 1
    answer.append(j)
    answer.append(h)
    return answer

# 다른 사람의 풀이
# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer
